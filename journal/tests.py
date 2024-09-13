from django.test import TestCase
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.


class SignupViewTests(TestCase):
    """
    Test cases for the signup view.
    """
    def test_signup_get(self):
        """
        Test that the signup view returns a status code of 200.
        """
        response = self.client.get(reverse('journal:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIsInstance(response.context['form'], UserRegistrationForm)

    def test_signup_post_valid(self):
        """
        Test that the signup view creates new user when form is valid.
        """
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'test_user@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }
        response = self.client.post(reverse('journal:signup'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('journal:login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def tes_signup_post_invalid(self):
        """
        Test that the signup view doesm't create new user when form is invalid.
        """
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'test_user@example.com',
            'password': 'testpassword',
            'confirm_password': 'wrongpassword'
        }
        response = self.client.post(reverse('journal:signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        # Get the form from the context
        form = response.context['form']

        # Check that the form is not valid
        self.assertTrue(form.errors)
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'], ['Passwords do not match.'])


class SignInViewTests(TestCase):
    """
    Test cases for the signin view.
    """
    def setUp(self):
        """
        Create a user for testing.
        """
        # Sign up a user
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'test_user@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }
        self.client.post(reverse('journal:signup'), data)

    def test_signin_get(self):
        """
        Test that the signin view returns a status code of 200.
        """
        response = self.client.get(reverse('journal:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signin_post_valid(self):
        """
        Test that the signin view logs in user when form is valid.
        """
        user = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        response = self.client.post(reverse('journal:login'), user)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('journal:home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_signin_post_invalid(self):
        """
        Test that the signin view does not log in user when form is invalid.
        """
        user = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }

        response = self.client.post(reverse('journal:login'), user)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
