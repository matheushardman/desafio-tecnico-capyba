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
        response = self.client.post(self.login_url, self.wrong_data, format="json")
        self.assertEqual(response.status_code, 401)

    def test_user_can_login_successfully(self):
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 200)
        