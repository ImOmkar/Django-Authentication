from django.urls import path
from .views import frontpage

urlpatterns = [
    path('', frontpage, name="frontpage")
]