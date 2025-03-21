from django.urls import path

from .views import home_as_view, travel_as_view


urlpatterns = [
    path('', home_as_view, name='home'),
    path('travel/', travel_as_view, name='travel'),
]
