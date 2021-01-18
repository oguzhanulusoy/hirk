from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .properties import *

import logging

logging.basicConfig(filename='user_app.log', format='%(asctime)s - %(levelname)s - %(message)s')


def logon(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user, None)
        logging.info(user_error_0001.format(username))
        return redirect('/')
    else:
        logging.error(user_error_0003.format(username))
        return redirect('/error')

    return None


def logout(request):
    logout(request)
    logging.info(user_error_0004.format(request.user.username))
    return redirect('/logon')


def forgot_password(request):
    return None
