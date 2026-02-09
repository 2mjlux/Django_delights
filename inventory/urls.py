from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='inventory/login.html'),
        name='login'),
    path('logout/', LogoutView.as_view(template_name='inventory/logout.html'),
        name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('inventory/', views.IngredientListView.as_view(), name='inventory'),
    path('menu/', views.MenuItemListView.as_view(), name='menu'),
    path('sales/', views.SaleListView.as_view(), name='sales'),
    path('reports/', views.ReportsView.as_view(), name='reports'),

    # Form URLs
    path('ingredient/add/', views.IngredientCreateView.as_view(),
         name='ingredient-add'),
    path('ingredient/<pk>/update/', views.IngredientUpdateView.as_view(),
         name='ingredient-update'),
    path('menuitem/add/', views.MenuItemCreateView.as_view(), name='menuitem-add'),
    path('reciperequirement/add/', views.RecipeRequirementCreateView.as_view(),
         name='reciperequirement-add'),
    path('sale/add/', views.SaleCreateView.as_view(), name='sale-add'),
]
