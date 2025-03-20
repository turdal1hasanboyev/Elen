from apps.category.models import Category


def object(request):
    """
    This function returns a dictionary with the object's attributes.
    """

    footer_categories = Category.objects.filter(is_active=True).order_by('?')

    context = {
        'footer_categories': footer_categories[:4],
    }

    return context
