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
        response = self.client.get(reverse('focus_timer:timer'))  # Use the correct URL name for your view
        self.assertEqual(response.status_code, 200)

    def test_timer_view_template_used(self):
        """
        Test that the correct template is used for the timer view.
        """
        response = self.client.get(reverse('focus_timer:timer'))  # Use the correct URL name for your view
        self.assertTemplateUsed(response, 'focus_timer/timer.html')

    # def test_timer_view_context(self):
    #     """
    #     Test that the context contains expected variables (if any).
    #     """
    #     response = self.client.get(reverse('timer'))  
    # # Use the correct URL name for your view
    #     # Check for specific context variables if needed
    #     # self.assertContains(response, 'expected_content')
