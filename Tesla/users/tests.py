from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class RegistrationTest(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'test',
            'password1': 'test123',
            'password2': 'test123'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(User.objects.filter(username='testuser').exists()) 