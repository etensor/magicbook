from django import forms
from .models import AiAnswer,Dream
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormDream(forms.Form):
    # usar_ejemplo = forms.BooleanField(required=False)

    ejemplo_prompt = '''titanical cyborg giant squid 
escaping alien toxic vegetation, 
intricate Three-point lighting portrait, 
by Ching Yeh and Greg Rutkowski, detailed cyberpunk 
in the style of GitS 1995'''

    prompt = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": "5", 'class': 'dreamprompt',
                   'placeholder': ejemplo_prompt}
        ),
        required=True, min_length=16
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prompt'].label = 'Ingresa una descripción detallada.'

    # probando para validar y usar un berraco ejemplo ehh -> near to impossible.
    ''' 
    def clean_prompt(self):
        usar_prompt_example = self.cleaned_data.get('prompt')
        if usar_prompt_example:
            data = self.data.copy()
            data.cleaned_data['prompt'] = self.ejemplo_prompt
            return data
        else:
            return self.cleaned_data['prompt']

    '''
    ''' 
    def clean(self):
        data = self.cleaned_data
        if data.get('usar_ejemplo'):
            if data.get('prompt') == '':
                new_data = self.data.copy()
                new_data['prompt'] = self.ejemplo_prompt
                return new_data
            else:
                raise forms.ValidationError(_('Usando el ejemplo revierte los cambios que hayas escrito'))
        else:
            if len(data.get('prompt')) < 16:
                raise forms.ValidationError(_('Trata de dar más detalles, entre más, mejor.'))
            else:
                return data
    '''

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


class NewDreamForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control opacity-75',
                'style': 'height: fit-content; \
                    text-align: center; width: 75%; margin: auto;',
            },
        ), required=True
    )
    is_public = forms.BooleanField(required=True)

    def form_valid(self, form):
        form.instance.userId = self.request.user
        return super().form_valid(form)

    class Meta:
        model = Dream
        fields = ['title', 'is_public']
