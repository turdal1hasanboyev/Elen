from django.urls import path

from .views import home_as_view, travel_as_view, photography_page_view, about_page_view


urlpatterns = [
    path('', home_as_view, name='home'),
    path('travel/', travel_as_view, name='travel'),
    path('photography/', photography_page_view, name='photography'),
    path('about/', about_page_view, name='about'),
]
