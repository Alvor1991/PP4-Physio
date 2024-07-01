from django.shortcuts import render, redirect
from .models import About, ContactRequest
from .forms import ContactForm
from django.contrib import messages

def about_me(request):
    """
    Renders the About page and handles the contact form submission
    """
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your message has been sent successfully.'
            )
            return redirect('about')

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form
        },
    )


