# landing/tests.py
from django.test import TestCase
from django.urls import reverse

class LandingViewTests(TestCase):
    
    def test_index_view(self):
        # Call the view
        response = self.client.get(reverse('index'))  # Replace 'index' with your URL name

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template was used
        self.assertTemplateUsed(response, 'landing/index.html')

        # Optionally, check if the page contains specific content
        self.assertContains(response, "Welcome to the Landing Page")
