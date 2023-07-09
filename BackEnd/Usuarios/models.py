from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        Admin = "Admin", "Administrador"
        CMS = "CMS", _("Community Manager")
        
        
    class Genero(models.TextChoices):
        MASCULINO = "MASCULINO", "Masculino"
        FEMENINO = "FEMENINO", "Femenino"
        NO_BINARIO = "NO_BINARIO", "No Binario"
        TRANSGENERO = "TRANSGENERO", "Transgénero"
        INTERSEX = "INTERSEX", "Intersex"
        NOT_SAY = "NOT_SAY", "Prefiero no Decirlo"

    
    base_role = Role.Admin
    
    numero_identificacion = models.CharField(
        default="",
        max_length=18,
        unique=True,
        verbose_name="Documento de Identificación",
    )
    second_name = models.CharField(
        default="", max_length=20, blank=True, null=False, verbose_name="Segundo nombre"
    )
    second_last_name = models.CharField(
        default="",
        max_length=20,
        blank=True,
        null=False,
        verbose_name="Segundo Apellido",
    )
    email = models.EmailField(_("email address"), max_length=255)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,12}$",
        message=_(
            "El Número debe tener 10 digitos \n ó 12 en el formato '+593 xx xxx'"
        ),
    )
    phone_no = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to=f"profile_pictures/", blank=True,)

    is_working = models.BooleanField(default=True)
    servicio = models.CharField(max_length=50, choices=Role.choices)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=100, choices=Genero.choices)

    USERNAME_FIELD = "numero_identificacion"
    REQUIRED_FIELDS = ["username", "email"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def save(self, *args, **kwargs):
        # Si el suaurio no ha sido creado(no tiene pk)
        if not self.pk:
            pass
        self.servicio = self.base_role
        
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return str(
            f"{self.first_name} {self.second_name} {self.last_name} {self.second_last_name}"
        )

    def get_short_name(self):
        return str(f"{self.first_name} {self.last_name}")

    
    def __str__(self):
        return str(f"Usuario: {self.username}")

