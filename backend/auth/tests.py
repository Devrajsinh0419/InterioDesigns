from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/auth/register/'
        self.login_url = '/auth/login/'

    def test_register_user_success(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'StrongPassword123!'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')

    def test_login_user_success(self):
        User.objects.create_user(username='testuser2', email='testuser2@example.com', password='StrongPassword123!')
        data = {
            'username': 'testuser2',
            'password': 'StrongPassword123!'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)

    def test_login_user_with_email_success(self):
        User.objects.create_user(username='testuser3', email='testuser3@example.com', password='StrongPassword123!')
        data = {
            'username': 'testuser3@example.com',
            'password': 'StrongPassword123!'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
