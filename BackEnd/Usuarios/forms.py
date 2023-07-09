from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from .models import User
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    numero_identificacion = forms.CharField(max_length=18)
    servicio = forms.CharField(max_length=12)
    email = forms.EmailField(label=_("email address"))
    # jefe = forms.BooleanField()
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message=_("Phone number must be entered in the format: '+593 ...'"))
    # phone_no = forms.CharField(validators=[phone_regex], max_length=15)
    # profile_picture = forms.ImageField()

    # is_working = forms.BooleanField()
    # servicio = forms.CharField(max_length=50)
    # fecha_de_nacimiento = forms.DateField()
    # genero = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("numero_identificacion", "email", "password")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "numero_identificacion",
            "first_name",
            "last_name",
            "email",
            "servicio",
            "phone_no",
            "fecha_de_nacimiento",
            "genero",
            "profile_picture",
        )
