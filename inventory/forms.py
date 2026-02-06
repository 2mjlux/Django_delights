from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Sale


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'price_per_unit']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'price']


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ['menu_item', 'ingredient', 'quantity']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['menu_item']

    def clean_menu_item(self):
        menu_item = self.cleaned_data['menu_item']

        # Check if enough ingredients in inventory
        for req in menu_item.reciperequirement_set.all():
            if req.ingredient.quantity < req.quantity:
                raise forms.ValidationError(
                    f"Not enough {req.ingredient.name} in inventory. "
                    f"Need {req.quantity} {req.ingredient.unit}, "
                    f"only have {req.ingredient.quantity} {req.ingredient.unit}."
                )

        return menu_item
