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
        else:
            messages.error(request, 'Please enter your email address.')

        return redirect('travel')
    

travel_as_view = TravelPageView.as_view()

def photography_page_view(request):
    """
    A view that renders the photography page.
    """

    photography_blogs = Blog.objects.filter(
        is_active=True,
        category__slug__exact='photography',
    ).order_by(
        'id',
    )

    context = {
        'photography_blogs': photography_blogs[:12],
    }

    return render(request=request, template_name='photography.html', context=context)

def about_page_view(request):
    """
    A view that renders the about page.
    """

    return render(request, 'about.html')


class FashionPageView(View):
    """
    A view that renders the fashion page.
    """

    template_name = 'fashion.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests.
        """

        fashion_blogs = Blog.objects.filter(is_active=True, category__slug__exact='fashion').order_by('id')

        context = {
            'fashion_blogs': fashion_blogs[:12],
        }

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests.
        """

        sub_email = request.POST.get('sub_email')

        url = request.build_absolute_uri()

        if sub_email:
            SubEmail.objects.create(sub_email=sub_email)
            messages.success(request, 'Your email has been successfully subscribed.')
        else:
            messages.error(request, 'Please enter your email address.')

        return redirect(url)
    

fashion_as_view = FashionPageView.as_view()
