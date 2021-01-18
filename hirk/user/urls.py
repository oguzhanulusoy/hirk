from django.urls import path
from .views import *
from .services import *

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('forgot-password/', forgot_password_view, name='forgot_password_view'),

    path('services/logon', logon, name="logon_service"),
    path('services/logout', logout, name="logout_service"),
    path('services/forgot_password', forgot_password, name="forgot_password_service"),

]
