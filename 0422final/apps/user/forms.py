from django import forms
from django.contrib.auth import authenticate
from user.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50,
                            label='E-mail',
                            widget=forms.EmailInput())
    password  = forms.CharField(max_length = 200,
                                 label='Password',
                                 widget = forms.PasswordInput())
    confirm_password  = forms.CharField(max_length = 200,
                                 label='Confirm',
                                 widget = forms.PasswordInput())



    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username

    # def clean_email(self):
    #     # Confirms that the username is not already present in the
    #     # User model database.
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email__exact=email):
    #         raise forms.ValidationError("The E-mail address is already taken.")
    #
    #     # We must return the cleaned data we got from the cleaned_data
    #     # dictionary
    #     return email

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        # return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 200, widget = forms.PasswordInput())

    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()

        # Confirms that the two password fields match
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username/password. Or please check your email and active your account.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data

