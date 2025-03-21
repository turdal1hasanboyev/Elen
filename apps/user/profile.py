from django.shortcuts import render

from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    """
    View to display user's profile information.
    """

    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and renders the profile template.
        """

        user = request.user

        context = {
            'user': user,
        }
        
        return render(request, self.template_name, context)
