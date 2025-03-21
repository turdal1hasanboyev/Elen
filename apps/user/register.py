from django.views import View

from django.shortcuts import render, redirect

from django.contrib.auth import login

from django.contrib import messages

from .models import CustomUser


class RegisterView(View):
    """
    View to handle user registration.
    """

    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        """
        Render the registration template.
        """

        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        """
        Handle the registration form submission.
        """
        
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            image=image,
            password=password,
        )
        user.save()
        messages.success(request, 'Registration successful')
        login(request, user)
        return redirect('profile')
    