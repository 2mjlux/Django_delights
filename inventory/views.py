from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Ingredient, MenuItem, Sale, RecipeRequirement
from django.db.models import Sum
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, SaleForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"
    context_object_name = "ingredients"


class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"
    context_object_name = "menu_items"


class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = "inventory/sale_list.html"
    context_object_name = "sales"


class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all sales
        sales = Sale.objects.all()

        # Calculate total revenue
        revenue = sum(sale.menu_item.price for sale in sales)

        # Calculate total cost
        cost = 0
        for sale in sales:
            for req in sale.menu_item.reciperequirement_set.all():
                cost += req.quantity * req.ingredient.price_per_unit

        # Calculate profit
        profit = revenue - cost

        # Pass to template
        context['revenue'] = revenue
        context['cost'] = cost
        context['profit'] = profit
        context['total_sales'] = sales.count()

        return context


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_form.html"
    success_url = reverse_lazy('inventory')


class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menuitem_form.html"
    success_url = reverse_lazy('menu')


class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirement_form.html"
    success_url = reverse_lazy('menu')


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = "inventory/sale_form.html"
    success_url = reverse_lazy('sales')

    def form_valid(self, form):
        # Save the sale first
        response = super().form_valid(form)

        # Get the menu item that was sold
        menu_item = form.cleaned_data['menu_item']

        # Deduct ingredients from inventory
        for req in menu_item.reciperequirement_set.all():
            ingredient = req.ingredient
            ingredient.quantity -= req.quantity
            ingredient.save()

        return response


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_form.html"
    success_url = reverse_lazy('inventory')
