from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Curso, Categoria, Profesionista, Post, Paciente

class ContactForm(forms.Form):
    name = forms.CharField()
    emal = forms.CharField();
    message = forms.CharField(widget = forms.Textarea)

    def send_email(self):
        pass

class RegistroCursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'

class ProfesionistaForm(UserCreationForm):
    REPORTES = (
    ('SI', 'Si'),
    ('NO', 'No'),
    )
    reportes = forms.ChoiceField(choices = REPORTES)
    horario_inicio = forms.TimeField()
    horario_final = forms.TimeField()
    telefono = forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'


class User_form(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
    is_superuser = forms.BooleanField(required = False, widget=forms.widgets.CheckboxInput())

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1','password2', 'is_superuser']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['creado']
