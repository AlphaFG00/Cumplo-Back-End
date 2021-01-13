from .views import CurrenciesListAPIView
from django.urls import path

urlpatterns = [
    
    path('currencies/', CurrenciesListAPIView.as_view())

]

