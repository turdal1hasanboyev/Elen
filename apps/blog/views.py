from django.shortcuts import render

from django.views import View

from apps.blog.models import Blog


class HomePageView(View):
    """
    A view that renders the home page.
    """

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests.
        """

        blogs = Blog.objects.filter(is_active=True).order_by('-created_at')

        context = {
            'blogs': blogs[:12],
        }

        return render(request, self.template_name, context)
    

home_as_view = HomePageView.as_view()
