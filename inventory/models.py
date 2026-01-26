from django.db import models


# Create your models here.
class Ingredient(models.Model):
    """
    Represents an ingredient in the restaurant's inventory.
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)  # e.g. "g", "count"
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Represents an item on the restaurant's menu.
    """
    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class RecipeRequirement(models.Model):
    """
    Represents an in indredient required for a menu item and its quantity.
    Links MenuItem to Ingredient (many-to-many relationship).
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (
            f"{self.menu_item.title} requires {self.quantity}"
            f"{self.ingredient.unit} of {self.ingredient.name}"
        )


class Sale(models.Model):
    """
    Represents the sale of a menu item to a customer.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.menu_item.title} at {self.timestamp}"
