from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from hirk.hirk.settings import LOGIN_URL as login_url
from hirk.hirk.properties import *

import logging

logging.basicConfig(filename='logs/user_app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if not user.is_active:
            login(request, user)
            logging.info(user_0001.format(username))
            return redirect('/')
        else:
            logging.error(user_0002.format(username))
            return redirect('/')
    else:
        logging.error(user_0003.format(username))
        return redirect('/login')

    return None


@login_required(login_url=login_url)
def logout(request):
    username = request.username
    logout(request)
    logging.info(user_0004.format(username))
    return redirect('/')


@login_required(login_url=login_url)
@permission_required()
def delete_user(request):
    user_id = request.POST['user_id']
    user = User.objects.filter(id=user_id)

    if not user.exists():
        logging.error(user_0005.format(user_id))
        return redirect('/error')

    user.delete()
    logging.info(user_0006.format(user_id, request.user.id))
    return redirect('/success')


def add_user(request):
    return None


def update_user(request):
    return None


@login_required(login_url=login_url)
@permission_required()
def get_all_users(request):
    users = User.objects.all()
    return users


@login_required(login_url=login_url)
@permission_required()
def get_user_by_id(request, id=None):
    user = User.objects.filter(id=id)

    if not user.exists():
        logging.error(user_0005.format(id))
        return redirect('/error')

    return user
