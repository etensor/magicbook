from pprint import pprint

from django.http import HttpResponse  # HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.template import loader
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

# from django.urls import reverse
# from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

from .forms import UserRegistrationForm, FormDream, FormJsonAPIS
from .models import Usuario, AiAnswer

from .stablediff import generarImagen
from os import environ as env_keys

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
            # asi guardamos variables en la sesion
            request.session['recien_registrado'] = True

            # Enviando correo de bienvenida

            send_mail(
                subject='Bienvenido a magicbook',
                message='\nTu cuenta ha sido creada,\n\tempieza ahora a crear arte.',
                from_email=env_keys['EMAIL_USER'],
                recipient_list=[usuario.email],
                auth_user=env_keys['EMAIL_USER'],
                auth_password=env_keys['EMAIL_PASS'],
                connection=None,
                html_message=None,
                fail_silently=True
            )

            messages.success(request, f'Bienvenido, {username}.\nTu cuenta ha sido creada.')
            # return HttpResponseRedirect(reverse('home', kwargs={context}))
            return redirect('home')
    else:
        formato = UserRegistrationForm()
    return render(request, 'register.html', {'form': formato})



# vincula el login con el perfil
# redirige si no hay sesion iniciada

@login_required()
def perfil(request, username):
    img_url = ''
    if request.method == 'POST':

        current_user = Usuario.objects.get(username=request.user.username)
        if 'save_prompt' in request.POST:
            formato = FormDream(request.POST)
            if formato.is_valid():
                messages.info(request, f' Generando imagen...')
                img_url = generarImagen(formato.cleaned_data.get('prompt'))
            context = {
                'form_prompt': formato,
                'img_generada': img_url[0]
            }
            #new_prompt = AiAnswer()

            return render(request, 'profile.html', context)

        if 'save_apis' in request.POST:
            new_apis = FormJsonAPIS(request.POST)
            apis_json = {}
            if new_apis.is_valid():
                apis_json = new_apis.cleaned_data.get('api_keys')
                current_user.api_keys = apis_json
                current_user.password = request.user.password
                current_user.save()
            context = {
                'form_apis': new_apis,
                'user_apikeys': apis_json,
            }
            return render(request, 'profile.html', context)

        elif 'delete_apis' in request.POST:
            current_user.api_keys = {}
            current_user.save()
            return render(request, 'profile.html')

    else:
        formato = FormDream()
        new_apis = FormJsonAPIS()

        usuario = Usuario.objects.get(username=username)
        user_apis = None
        if usuario.api_keys:
            user_apis = usuario.api_keys
            # load api_keys as env vars -> comunicación con services
            for key, value in user_apis.items():
                if isinstance(value, bool): # env vars no pueden ser true/false.
                    continue
                env_keys[key] = value


        context = {
            'form_prompt': formato,
            'form_apis': new_apis if 'save_apis' in request.POST else None,
            'user_apikeys': json.dumps(user_apis) if user_apis else None
        }
        return render(request, 'profile.html', context)


class ChangePassView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')
    success_message = "Tu contraseña ha sido cambiada."


class ResetPassView(SuccessMessageMixin, PasswordResetView):
    template_name = 'reset_password.html'
    success_url = reverse_lazy('home')
    success_message = 'A tu correo fueron enviadas las instrucciones para \n \
                       reestablecer tu contraseña.'


def prompts_json(request):
    data_prompts = list()


def user_page(request, user_id):
    res = f"Tu usuario es: {user_id}, que tal"
    return HttpResponse(res)




