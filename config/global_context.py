from apps.category.models import Category, Tag
from apps.blog.models import Blog


def object(request):
    """
    This function returns a dictionary with the object's attributes.
    """

    footer_categories = Category.objects.filter(is_active=True).order_by('?')
    rside_categories = Category.objects.filter(is_active=True).order_by('?')
    rside_popular_articles = Blog.objects.filter(is_active=True).order_by('views')
    rside_tags = Tag.objects.filter(is_active=True).order_by('?')

    context = {
        'footer_categories': footer_categories[:4],
        'rside_categories': rside_categories[:5],
        'rside_popular_articles': rside_popular_articles[:3],
        'rside_tags': rside_tags[:8],
    }

    return context
