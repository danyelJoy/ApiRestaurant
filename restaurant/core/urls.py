from django.urls import path
from .views import RestaurantView

urlpatterns = [
    path('restaurants/', RestaurantView.as_view(), name='restaurants_list'),
    path('restaurants/<int:id>', RestaurantView.as_view, name='restaurants_process')
]
