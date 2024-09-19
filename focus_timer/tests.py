from django.test import TestCase, Client
from django.urls import reverse


class TimerViewTests(TestCase):
    """
    Test cases for the timer view.
    """
    def setUp(self):
        """
        Set up the test client.
        """
        self.client = Client()

    def test_timer_view_status_code(self):
        """
        Test that the timer view returns a status code of 200.
        """
        response = self.client.get(reverse('focus_timer:timer'))
        self.assertEqual(response.status_code, 200)

    def test_timer_view_template_used(self):
        """
        Test that the correct template is used for the timer view.
        """
        response = self.client.get(reverse('focus_timer:timer'))
        self.assertTemplateUsed(response, 'focus_timer/timer.html')
