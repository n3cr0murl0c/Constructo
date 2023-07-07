from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from Usuarios.models import *
from Usuarios.forms import *

# Register your models here.
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm  # Form for change view
    model = User
    list_display = ["numero_identificacion", "email"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Información Personal",
            {
                "fields": (
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
            },
        ),
        (
            "Permisos",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during foo creation
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def save_model(self, request, obj, form, change):
        # SUCCESS ACTIONS
        # obj.subscriptionInfo.paid = 1
        # obj.subscriptionInfo.save()
        obj.save()
