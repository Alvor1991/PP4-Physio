from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_signup_redirect_url(self, request):
        """
        Return the URL to redirect to after a successful signup.
        """
        return reverse('user_appointments')  # Redirect to appointments page

    def add_message(self, request, level, message_template,
                    message_context=None, extra_tags=''):
        # List of messages to suppress
        suppressed_messages = [
            'account/messages/email_confirmation_sent.txt',
            'account/messages/logged_out.txt',
            'account/messages/logged_in.txt',
            'account/messages/signed_up.txt',
            'account/messages/email_verified.txt',
        ]

        # Suppress specific messages by checking against the list
        if message_template in suppressed_messages:
            return

        # Call the superclass method for other messages
        super().add_message(request, level, message_template,
                            message_context, extra_tags)
