from django.contrib import admin

from .models import SubEmail


admin.site.site_header = "Elen Admin Panel"
admin.site.site_title = "Elen Admin Panel"
admin.site.index_title = "Welcome to Elen Admin Panel!"


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    """
    SubEmail Admin Model
    """

    model = SubEmail

    ordering = ('id',)
    list_display = (
        'id',
        'sub_email',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
    search_fields = ('sub_email',)

    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )

    fieldsets = (
        ("Basic Information", {
            "fields": ("sub_email", "is_active",),
        }),
        ("Meta Data", {
            "fields": ("id", "created_at", "updated_at",),
            "classes": ("collapse",),
        }),
    )
