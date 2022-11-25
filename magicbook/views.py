from django.http import HttpResponse  # HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.urls import reverse
# from django.contrib.auth import login
# from django.contrib.auth import views as auth_view

from .forms import UserRegistrationForm, FormDream, FormJsonAPIS
from .models import Usuario
from .stablediff import generarImagen
from os import environ as env_keys
from pprint import pprint

import json
# Create your views here.


def home(request):
    template = loader.get_template('home.html')
    context = { 'usuario': "anonymous"} # request.session['usuario']}

    if request.user.is_authenticated:
        context['usuario'] = request.user.username
    return HttpResponse(template.render(
        context, request
    ))


def register(request):
    username = ""
    if request.method == 'POST':
        # formato = UserCreationForm(request.POST)
        formato = UserRegistrationForm(request.POST)
        if formato.is_valid():
            formato.save()
            usuario = Usuario(
                username=formato.cleaned_data.get('username'),
                email=formato.cleaned_data.get('email'),
                password=formato.cleaned_data.get('password1')
            )
            usuario.save()
            username = formato.cleaned_data.get('username')
            messages.success(request, f'Bienvenido, {username}.\nTu cuenta ha sido creada.')
            # asi guardamos variables en la sesion
            request.session['recien_registrado'] = True
            # return HttpResponseRedirect(reverse('home', kwargs={context}))
            return redirect('home')
    else:
        formato = UserRegistrationForm()
    return render(request, 'register.html', {'form': formato})



# vincula el login con el perfil
# redirige si no hay sesion iniciada

@login_required()
def perfil(request,username):
    img_url = ''
    if request.method == 'POST':

        current_user = Usuario.objects.get(username=request.user.username)
        if 'save_prompt' in request.POST:
            formato = FormDream(request.POST)
            if formato.is_valid():
                messages.success(request, f' Generando imagen...')
                img_url = generarImagen(formato.cleaned_data.get('prompt'))
            context = {
                'form_prompt': formato,
                'img_generada': img_url[0]
            }

            return render(request, 'profile.html', context)

        if 'save_apis' in request.POST:
            new_apis = FormJsonAPIS(request.POST)
            apis_json = {}
            if new_apis.is_valid():
                apis_json = json.loads(new_apis.cleaned_data.get('api_keys'))
                current_user.api_keys = apis_json
                current_user.save()
            context = {
                'form_apis': new_apis,
                'user_apikeys': apis_json,
            }
            return render(request, 'profile.html', context)

    else:
        formato = FormDream()
        new_apis = FormJsonAPIS()

        usuario = Usuario.objects.get(username=username)
        user_apis = {}
        if usuario.api_keys:
            user_apis = usuario.api_keys
            # load api_keys as env vars -> comunicación con services
            for key, value in user_apis.items():
                env_keys[key] = value

        context = {
            'form_prompt': formato,
            'form_apis': new_apis,
            'user_apikeys': user_apis
        }
        return render(request, 'profile.html', context)




def user_page(request, user_id):
    res = f"Tu usuario es: {user_id}, que tal"
    return HttpResponse(res)






