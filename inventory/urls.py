from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('inventory/', views.IngredientListView.as_view(), name='inventory'),
    path('menu/', views.MenuItemListView.as_view(), name = 'menu'),
    path('sales/', views.SaleListView.as_view(), name = 'sales'),
    path('reports/', views.ReportsView.as_view(), name = 'reports'),
]
