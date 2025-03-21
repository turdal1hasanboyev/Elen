from django.shortcuts import render, redirect

from django.contrib import messages

from django.views import View

from .models import Contact


class ContactPageView(View):
    """
    View for the contact page.
    """

    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        """
        Render the contact page template.
        """

        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        """
        Handle form submission.
        """

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            contact = Contact()
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()
            messages.success(request, 'Your message has been sent successfully.')
        else:
            messages.error(request, 'Please fill in all fields.')

        return redirect('contact')
    

contact_as_view = ContactPageView.as_view()
