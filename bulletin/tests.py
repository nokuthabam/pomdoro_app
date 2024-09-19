from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BulletinBoard, Note, Image
from .forms import NoteForm, ImageForm
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from PIL import Image as PilImage


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

    def test_delete_board_view_status_code(self):
        """
        Test that the delete board view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        board_user = User.objects.get(username='testuser')
        bulletin_board = BulletinBoard.objects.create(
            title='Test Board', description='Test Description',
            user=board_user)
        response = self.client.get(reverse('bulletin:delete_board',
                                           args=[bulletin_board.id]))
        self.assertEqual(response.status_code, 200)


class NoteTests(TestCase):
    """
    Test cases for the note.
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

    def test_note_form_valid(self):
        """
        Test that the note form is valid.
        """
        form = NoteForm(data={'content': 'Test Content'})
        self.assertTrue(form.is_valid())

    def test_add_note_view_status_code(self):
        """
        Test that the add note view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        board_user = User.objects.get(username='testuser')
        bulletin_board = BulletinBoard.objects.create(
            title='Test Board', description='Test Description',
            user=board_user)
        response = self.client.get(reverse('bulletin:add_note',
                                           args=[bulletin_board.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_note_view_status_code(self):
        """
        Test that the delete note view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        bulletin_board = BulletinBoard.objects.create(
            title='Test Board', description='Test Description',
            user=User.objects.get(username='testuser'))
        note = Note.objects.create(content='Test Content',
                                   bulletin_board=bulletin_board)
        response = self.client.get(reverse('bulletin:delete_note',
                                           args=[note.id]))
        self.assertEqual(response.status_code, 302)


class ImageTests(TestCase):
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

    def test_image_form_valid(self):
        """
        Test that the image form is valid.
        """
        # Create a mock image file using PIL (now referred to as PilImage) and BytesIO
        image = io.BytesIO()
        PilImage.new('RGB', (100, 100)).save(image, format='JPEG')
        image.seek(0)
        
        # Create a SimpleUploadedFile to simulate image upload
        uploaded_image = SimpleUploadedFile('test_image.jpg', image.read(),
                                            content_type='image/jpeg')

        # Pass the uploaded image to the form
        form = ImageForm(data={}, files={'image': uploaded_image})
        self.assertTrue(form.is_valid())

    def test_add_image_view_status_code(self):
        """
        Test that the add image view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        board_user = User.objects.get(username='testuser')
        bulletin_board = BulletinBoard.objects.create(
            title='Test Board', description='Test Description',
            user=board_user)
        response = self.client.get(reverse('bulletin:add_image',
                                           args=[bulletin_board.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_image_view_status_code(self):
        """
        Test that the delete image view returns a status code of 200.
        """
        self.client.login(username='testuser', password='testpassword')
        bulletin_board = BulletinBoard.objects.create(
            title='Test Board', description='Test Description',
            user=User.objects.get(username='testuser'))
        image = Image.objects.create(image='Test Image',
                                     bulletin_board=bulletin_board)
        response = self.client.get(reverse('bulletin:delete_image',
                                           args=[image.id]))
        self.assertEqual(response.status_code, 302)
