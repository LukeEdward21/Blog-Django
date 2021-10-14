from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Dados pessoais", {"fields": ("image", "birth_date", "gender", )}),
        ("Permissões", {"fields": ("is_writer", )}),
    )

    add_fieldsets = auth_admin.UserAdmin.add_fieldsets + (
        ("Informações pessoais", {"fields": ("first_name", "last_name", "email", "birth_date", "gender")}),
        ("Perfil do usuário", {"fields": ("image", )}),
        ("Permissões", {"fields": ("is_writer", )}),
    )

    readonly_fields = ['birth_date']
