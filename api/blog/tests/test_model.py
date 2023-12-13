from .test_setup import TestSetUp
from blog.models import User, BlogPost, RestrictBlogPost

class TestUserModels(TestSetUp):
    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(**self.user_data)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class TestBlogModels(TestSetUp):
    def test_create_blog_post(self):
        blog_post = BlogPost.objects.create(**self.blog_post_data)
        self.assertEqual(blog_post.title, self.blog_post_data['title'])
        self.assertEqual(blog_post.author, self.user)
        self.assertEqual(blog_post.content, self.blog_post_data['content'])
        self.assertFalse(blog_post.draft)

class TestRestrictBlogModels(TestSetUp):
    def test_create_restrict_blog_post(self):
        restrict_blog_post = RestrictBlogPost.objects.create(**self.restrict_blog_post_data)
        self.assertEqual(restrict_blog_post.title, self.restrict_blog_post_data['title'])
        self.assertEqual(restrict_blog_post.author, self.user)
        self.assertEqual(restrict_blog_post.content, self.restrict_blog_post_data['content'])
        self.assertFalse(restrict_blog_post.draft)