from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Blog Admin Model
    """

    model = Blog

    ordering = ('-id',)
    list_display = (
        'id',
        'name',
        'category',
        'image',
        'author',
        'views',
        'likes',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active', 'category', 'author',)
    search_fields = ('name',)

    prepopulated_fields = {'slug': ('name',),}

    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", 'slug', 'category', 'tags', 'description', 'image', 'author', 'views', 'likes', "is_active",),
        }),
        ("Meta Data", {
            "fields": ("id", "created_at", "updated_at",),
            "classes": ("collapse",),
        }),
    )
