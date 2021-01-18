from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .properties import *
import logging

template_dir = 'user/'
logging.basicConfig(filename='user_app.log', format='%(asctime)s - %(levelname)s - %(message)s')


def login_view(request):
    url = template_dir + 'login.html'
    context = {"user_message_0001": user_message_0001,
               "user_message_0002": user_message_0002,
               "user_message_0003": user_message_0003,
               "user_message_0004": user_message_0004,
               "user_message_0005": user_message_0005}

    return render(request, url, context)


@login_required()
def forgot_password_view(request):
    url = template_dir + 'forgot-password.html'
    context = {"user_message_0001": user_message_0001,
               "user_message_0005": user_message_0005,
               "user_message_0006": user_message_0006,
               "user_message_0007": user_message_0007,
               "user_message_0003": user_message_0003,
               "user_message_0008": user_message_0008
               }
    return render(request, url, context)
