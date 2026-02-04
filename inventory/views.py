from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Ingredient, MenuItem, Sale
from django.db.models import Sum


class HomeView(TemplateView):
    template_name = "inventory/home.html"


class IngredientListView(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"
    context_object_name = "ingredients"


class MenuItemListView(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"
    context_object_name = "menu_items"


class SaleListView(ListView):
    model = Sale
    template_name = "inventory/sale_list.html"
    context_object_name = "sales"


class ReportsView(TemplateView):
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
