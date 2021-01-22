import smtplib

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .properties import *
from django.core.mail import send_mail

import logging

logging.basicConfig(filename='user_app.log', format='%(asctime)s - %(levelname)s - %(message)s')


def signin(request):
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


def signout(request):
    logout(request)
    logging.info(user_error_0004.format(request.user.username))
    return redirect('/logon')


def forgot_password(request):
    email = request.POST.get('email')
    user = User.objects.get(email=email)

    send_mail(
        'Subject here',
        'Here is the message.',
        'ulusoiozi@gmail.com',
        ['ulusoyoguzhan@gmail.com'],
        fail_silently=False,
    )
    return None
