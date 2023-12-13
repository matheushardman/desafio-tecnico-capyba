from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register_successfully(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.data['name'], self.user_data['name'])
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.status_code, 201)
    
    def test_user_cannot_login_with_no_data(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, 400)

    def test_user_cannot_login_with_wrong_data(self):
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, self.wrong_data, format="multipart")
        self.assertEqual(response.status_code, 401)

    def test_user_can_login_successfully(self):
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_user_can_update_profile(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(self.login_url, self.user_data, format="json")
        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.patch(self.user_update_url, self.user_update_data, format="json")
        self.assertEqual(response.data['name'], self.user_update_data['name'])
        self.assertEqual(response.data['username'], self.user_update_data['username'])
        self.assertEqual(response.data['email'], self.user_update_data['email'])
        self.assertEqual(response.status_code, 200)

    def test_user_can_view_blog_list(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(self.login_url, self.user_data, format="json")
        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get(self.blog_list_url)
        self.assertEqual(response.status_code, 200)

    def test_user_can_create_blog_post(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(self.login_url, self.user_data, format="json")
        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.post(self.blog_list_url, self.blog_data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_user_can_view_blog_post_detail(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(self.login_url, self.user_data, format="json")
        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        create_response = self.client.post(self.blog_list_url, self.blog_data, format="json")
        blog_id = create_response.data['id']

        response = self.client.get(f'{self.blog_list_url}{blog_id}/')
        self.assertEqual(response.status_code, 200)

    def test_user_can_update_blog_post(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(self.login_url, self.user_data, format="json")
        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        create_response = self.client.post(self.blog_list_url, self.blog_data, format="json")
        blog_id = create_response.data['id']

        response = self.client.patch(f'{self.blog_list_url}{blog_id}/', self.blog_update_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_blog_post(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(self.login_url, self.user_data, format="json")
        token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        create_response = self.client.post(self.blog_list_url, self.blog_data, format="json")
        blog_id = create_response.data['id']

        response = self.client.delete(f'{self.blog_list_url}{blog_id}/')
        self.assertEqual(response.status_code, 204)