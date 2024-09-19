from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BulletinBoard, Note, Image
from .forms import NoteForm, ImageForm
from django.test import Client
from journal.forms import UserRegistrationForm


class BulletinBoardTests(TestCase):
    """
    Test cases for the bulletin board.
    """
    def setUp(self):
        """
        Set up the test client.
        """
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'test_user@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }
        self.client.post(reverse('journal:signup'), data)

    def test_home_view_status_code(self):
        """
        Test that the home view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('bulletin:home'))
        self.assertEqual(response.status_code, 200)

    def test_board_view_status_code(self):
        """
        Test that the board view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        board_user = User.objects.get(username='testuser')
        bulletin_board = BulletinBoard.objects.create(
            title='Test Board', description='Test Description',
            user=board_user)
        response = self.client.get(reverse('bulletin:board',
                                           args=[bulletin_board.id]))
        self.assertEqual(response.status_code, 200)

    def test_board_view_template_used(self):
        """
        Test that the correct template is used for the board view.
        """
        self.client.login(username='testuser', password='testpassword')
        board_user = User.objects.get(username='testuser')
        bulletin_board = BulletinBoard.objects.create(
            title='Test Board', description='Test Description',
            user=board_user)
        response = self.client.get(reverse('bulletin:board',
                                           args=[bulletin_board.id]))
        self.assertTemplateUsed(response, 'bulletin/board.html')

    def test_add_board_view_status_code(self):
        """
        Test that the add board view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('bulletin:add_board'))
        self.assertEqual(response.status_code, 200)

    def test_add_board_view_template_used(self):
        """
        Test that the correct template is used for the add board view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('bulletin:add_board'))
        self.assertTemplateUsed(response, 'bulletin/add_board.html')

