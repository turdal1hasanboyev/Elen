from django.shortcuts import render, redirect
from django.contrib import messages

from django.views import View

from apps.blog.models import Blog
from apps.common.models import SubEmail


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


class TravelPageView(View):
    """
    A view that renders the travel page.
    """

    template_name = 'travel.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests.
        """

        travel_blogs = Blog.objects.filter(is_active=True, category__slug__exact='travel').order_by('id')

        context = {
            'travel_blogs': travel_blogs[:5],
        }

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests.
        """

        sub_email = request.POST.get('sub_email')

        if sub_email:
            SubEmail.objects.create(sub_email=sub_email)
            messages.success(request, 'Your email has been successfully subscribed.')
            return redirect('travel')
    

travel_as_view = TravelPageView.as_view()
