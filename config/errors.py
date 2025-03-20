from django.shortcuts import render


def page_not_found_view(request, exception=None):
    """
    404 error view
    """

    return render(request, '404.html', status=404)
