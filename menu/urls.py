from django.urls import path
from .import views


app_name = 'menu'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # cafeteria/menu/
    path('menu/', views.DetailView.as_view(), name='detail'),

    # cafeteria/menu/vegetable/
    path('menu/Vegetable/', views.VegetableView.as_view(), name='Vegetable'),

    path('menu/Breads/', views.BreadsView.as_view(), name='Breads'),

    path('menu/Beverages/', views.BeveragesView.as_view(), name='Beverages'),

    path('menu/Plate/', views.PlateView.as_view(), name='Plate'),

    path('menu/Snacks/', views.SnacksView.as_view(), name='Snacks'),

    path('menu/Street Food/', views.StreetFoodView.as_view(), name='Street Food'),

    path('menu/Rice/', views.RiceView.as_view(), name='Rice'),

    path('menu/Desserts/', views.DessertsView.as_view(), name='Desserts'),



]
