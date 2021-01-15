from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from hirk.hirk.settings import LOGIN_URL as login_url
import logging
from hirk.hirk.properties import *

logging.basicConfig(filename='user_app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

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


'''
from django.contrib.auth.decorators import permission_required
@permission_required('polls.add_choice', login_url='/loginpage/')
'''