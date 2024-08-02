from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_signup_redirect_url(self, request):
        """
        Return the URL to redirect to after a successful signup.
        """
        return reverse('welcome')  # Use the name of your welcome page URL pattern

    def add_message(self, request, level, message_template, message_context=None, extra_tags=''):
        # Suppress the "Confirmation email sent" message
        if message_template == 'account/messages/email_confirmation_sent.txt':
            return
        # Suppress the "You have successfully signed out" message
        if message_template == 'account/messages/logged_out.txt':
            return
        super().add_message(request, level, message_template, message_context, extra_tags)
