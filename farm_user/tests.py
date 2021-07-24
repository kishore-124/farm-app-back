from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import User



# test setup

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            "user": {
                'username': 'test',
                'email': 'test@gmail.com',
                'password': 'password'
            }
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


# user register test cases

class RegisterViewsTest(TestSetUp):

    def test_user_can_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register_with_data(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.json()['email'], self.user_data['user']['email'])
        self.assertEqual(response.status_code, 201)

    def test_user_can_register_with_duplicate_user(self):
        User.objects.create(username="test", email="test@gmail.com", password="password")
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.json()['email'], ['user with this email already exists.'])
        self.assertEqual(response.status_code, 400)


# user login test cases

class LoginViewsTest(TestSetUp):

    def test_user_can_login_with_no_data(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_login_with_data(self):
        User.objects.create(username="test", email="test@gmail.com", password="test@12345")
        response = self.client.post(self.login_url, {'user': {'email': 'test@gmail.com', 'password': 'test@12345'}},
                                    format="json")
        self.assertEqual(response.status_code, 200)
