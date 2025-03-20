from django.contrib import admin

from .models import Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin Model
    """

    model = Category

    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'slug',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_active',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    prepopulated_fields = {
        'slug': ('name',),
    }

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "slug", "is_active",),
        }),
        ("Meta Data", {
            "fields": ("id", "created_at", "updated_at",),
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Tag Admin Model
    """

    model = Tag

    ordering = ('-id',)
    list_display = (
        'id',
        'name',
        'slug',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_active',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    
    prepopulated_fields = {
        'slug': ('name',),
    }

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "slug", "is_active",),
        }),
        ("Meta Data", {
            "fields": ("id", "created_at", "updated_at",),
        }),
    )
    