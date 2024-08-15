from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    """
    Custom signup form extending the default allauth SignupForm.
    Adds fields for username, first name, last name, and email.
    """
    username = forms.CharField(
        max_length=30, label='Username'
    )
    first_name = forms.CharField(
        max_length=30, label='First Name', required=False
    )
    last_name = forms.CharField(
        max_length=30, label='Last Name', required=False
    )
    email = forms.EmailField(
        required=True, label='Email'
    )

    class Meta:
        """
        Meta class to specify the fields that will be included in the form.
        """
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2'
        ]

    def save(self, request):
        """
        Saves user instance with additional fields (username, first/last name).
        Overrides the default save method to include custom fields.
        """
        user = super().save(request)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
