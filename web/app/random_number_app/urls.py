from django.urls import path
from .views import HomeView, NumberView


app_name = 'random_number_app'

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('number/', NumberView.as_view(), name='get_number'),
]
