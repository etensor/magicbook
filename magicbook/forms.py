from django import forms
from .models import AiAnswer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormDream(forms.Form):
    usar_ejemplo = forms.BooleanField()

    prompt = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": "5", 'class': 'dreamprompt',
                   'placeholder': '''titanical cyborg giant squid 
escaping alien toxic vegetation, 
intricate Three-point lighting portrait, 
by Ching Yeh and Greg Rutkowski, detailed cyberpunk 
in the style of GitS 1995''',
                   'value': ''},
        ),
        min_length=16
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prompt'].label = 'Ingresa una descripción detallada.'

    class Meta:
        model = AiAnswer
        fields = ['prompt']


# Heredamos y extendemos
# la forma default para incluir el correo.

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FormJsonAPIS(forms.Form):
    api_keys = forms.JSONField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control opacity-50',
                'style': 'height: 10vh;',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['api_keys']\
            .label = "Ingresa  tus llaves en formato JSON para los servicios de replicate (por ahora)"   # :D

    class Meta:
        model = User
        fields = ['api_keys']


    '''
    def clean_api_keys(self):
        return json.dumps(
            self.cleaned_data.get('api_keys'),
            sort_keys=True,
            indent=2,
            separators=(',', ':')
        )
    '''
