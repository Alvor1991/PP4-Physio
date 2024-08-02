from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    first_name = forms.CharField(max_length=30, label='First Name', required=False)
    last_name = forms.CharField(max_length=30, label='Last Name', required=False)
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, request):
        user = super().save(request)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
