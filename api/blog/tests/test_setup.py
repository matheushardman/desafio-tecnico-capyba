from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('create-user')
        self.login_url = reverse('token_obtain_pair')
        self.user_data={
            'name': 'email de email',
            'email': 'email@gmail.com',
            'username': 'email',
            'password': 'email555@gmail.com',
            'profile_photo': 'string'
        }
        self.wrong_data={
            'email': 'wrong@gmail.com',
            'password': 'wrong555@gmail.com'
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()