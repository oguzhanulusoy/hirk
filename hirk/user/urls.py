from django.urls import path
from .views import *

urlpatterns = [
    path('testim/', test_view, name='index')
]