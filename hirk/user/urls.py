from django.urls import path
from .views import *
from .services import *

urlpatterns = [
    path('login/', login_view, name='login_view'),

    path('services/logon', logon, name="logon"),
    path('services/logout', logout, name="logout"),
]
