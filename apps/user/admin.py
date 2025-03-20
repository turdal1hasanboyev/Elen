from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom User Admin Model
    """

    model = CustomUser

    ordering = ('id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
        'last_login',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'date_joined',
        'last_login',
    )

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password',),
        }),
        ("Personal Info", {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name',),
        }),
        ("Permissions", {
            'classes': ('wide',),
            'fields': ('is_superuser', 'is_staff', 'is_active',),
        }),
        ("Important Dates", {
            'classes': ('wide',),
            'fields': ('date_joined', 'last_login', 'created_at', 'updated_at',),
        }),
        ("ID", {
            'classes': ('wide',),
            'fields': ('id',),
        }),
    )

    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
        ("Permissions", {
            'classes': ('wide',),
            'fields': ('is_superuser', 'is_staff', 'is_active',),
        }),
    )
