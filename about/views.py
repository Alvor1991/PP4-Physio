from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .models import About, ContactRequest
from .forms import ContactForm

def about_me(request):
    """
    View to handle the 'About Me' page, including displaying the latest 'About' content 
    and handling the contact form submission.
    Displays an individual instance of :model:`about.About`
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Your message has been sent successfully. I endeavor to respond within 2 working days.")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})

    # Fetch the first About entry, since updated_on doesn't exist
    about = About.objects.first()
    contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form,
        },
    )