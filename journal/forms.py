from django import forms
from .models import JournalEntry
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE


class JournalEntryForm(forms.ModelForm):
    """
    A class used to represent a form for a journal entry
    Attributes:
        title (CharField): The title of the entry
        body (TextField): The body of the entry
    """

    class Meta:
        """
        A class used to represent the metadata of the form
        """
        model = JournalEntry
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'size': 80}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20})
        }


class UserRegistrationForm(forms.ModelForm):
    """
    A class used to represent a user registration form
    Attributes:
        first_name (CharField): The first name of the user
        last_name (CharField): The last name of the user
        username (CharField): The username of the user
        email (EmailField): The email of the user
        password (CharField): The password of the user
    """
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """
        A class used to represent the metadata of the form
        """
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password',
                  'confirm_password']

    def clean_username(self):
        """
        A function used to validate that the username is unique.
        Returns:
            username (str): The username of the user
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken')
        return username

    def clean_email(self):
        """
        A function used to validate that the email is unique.
        Returns:
            email (str): The email of the user
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already taken')
        return email

    def clean(self):
        """
        A function used to validate that the passwords match.
        Returns:
            cleaned_data (dict): The cleaned data
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

    def save(self):
        """
        A function used to save the user registration form
        Returns:
            user (User): The user object
        """
        user = User.objects.create_user(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],

        )
        user.save()
        return user
