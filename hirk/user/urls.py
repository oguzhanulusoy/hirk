from django.urls import path
from .views import *
from .services import *

urlpatterns = [
    path('signin/', signin_view, name='signin_view'),
    path('forgot-password/', forgot_password_view, name='forgot_password_view'),

    path('services/signin', signin, name="signin_service"),
    path('services/signout', signout, name="signout_service"),
    path('services/forgot_password', forgot_password, name="forgot_password_service"),

]
