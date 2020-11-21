from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User
from .models import AutoBrand, AutoModels, AutoCharacters, TechnicalService, TestDriveModel


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('phone', 'full_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'full_name', 'phone', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('email',)


@admin.register(AutoBrand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)


@admin.register(AutoModels)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('model_name',)


@admin.register(AutoCharacters)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'engine', 'power')


@admin.register(TechnicalService)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'brand', 'model', 'data', 'time', 'phone_number')


@admin.register(TestDriveModel)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'brand', 'model', 'data', 'time', 'phone_number')
