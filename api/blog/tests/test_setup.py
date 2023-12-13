from rest_framework.test import APITestCase
from django.urls import reverse
from blog.models import User

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('create-user')
        self.login_url = reverse('token_obtain_pair')
        self.user_update_url = reverse('edit-user')
        self.blog_list_url = reverse('blog-list')
        self.user_data={
            'name': 'email',
            'email': 'email@gmail.com',
            'username': 'email',
            'password': 'email555@gmail.com',
            'profile_photo': None
        }
        self.wrong_data={
            'email': 'wrong@gmail.com',
            'password': 'wrong555@gmail.com'
        }
        self.user_update_data = {
            'name': 'Updated Name',
            'username': 'Username',
            'email': 'username@mail.com',
            'profile_photo': None
        }
        self.blog_data = {
            'title': 'Test Blog Post',
            'content': 'Lorem ipsum dolor sit amet.',
            'draft': False 
        }
        self.blog_update_data = {
            'title': 'Updated Title',
            'content': 'Updated content.',
            'draft': True
        }
        self.user = User.objects.create_user(username='testauthor', email='author@example.com', password='testpassword')
        self.blog_post_data = {
            'title': 'Test Blog Post',
            'author': self.user,
            'content': 'Lorem ipsum dolor sit amet.',
            'draft': False
        }
        self.restrict_blog_post_data = {
            'title': 'Test Restrict Blog Post',
            'author': self.user,
            'content': 'Lorem ipsum dolor sit amet.',
            'draft': False
        }
        self.serializer_user_data = {
            'id': 1,
            'name': 'John Doe',
            'username': 'johndoe',
            'email': 'john@example.com',
            'password': 'testpassword',
            'profile_photo': None
        }
        self.serializer_blog_post_data = {
            'id': 1,
            'title': 'Test Blog Post',
            'author': 1,
            'content': 'Lorem ipsum dolor sit amet.',
            'create_at': '2023-01-01T12:00:00Z',
            'update_at': '2023-01-01T12:00:00Z',
            'draft': False
        }
        self.serializer_restrict_blog_post_data = {
            'id': 1,
            'title': 'Test Restrict Blog Post',
            'author': 1,
            'content': 'Lorem ipsum dolor sit amet.',
            'create_at': '2023-01-01T12:00:00Z',
            'update_at': '2023-01-01T12:00:00Z',
            'draft': False
        }

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()