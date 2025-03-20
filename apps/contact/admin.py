from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Contact Admin Model
    """

    model = Contact
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'email',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'email',
    )
    list_filter = (
        'is_active',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "email", 'subject', 'message', "is_active",),
        }),
        ("Metadata", {
            "fields": ("id", "created_at", "updated_at",),
        }),
    )
