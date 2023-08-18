from django.urls import path

from currency_app.views import show_rates

urlpatterns = [
    path('show_rates/', show_rates),
]