from django.test import TestCase

from users.models import User
from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.
class UsersTests(TestCase):
	def test_create_user(self):
		# bad request: password less then 8 digits
		response = self.client.post("/users/", {
			"email": "test@test.com",
			"username": "test",
			"password": "123"
		})
		self.assertEqual(response.status_code, 400)

		# bad request: username with special chars
		response = self.client.post("/users/", {
			"email": "test@test.com",
			"username": "test@* _dsa",
			"password": "123"
		})
		self.assertEqual(response.status_code, 400)

		# good request
		response = self.client.post("/users/", {
			"email": "test@test.com",
			"username": "test",
			"password": "12345678"
		})
		self.assertEqual(response.status_code, 201)

	def test_without_confirm_email(self):
		response = self.client.post("/users/", {
			"email": "test@test.com",
			"username": "test",
			"password": "12345678"
		})
		self.assertEqual(response.data['message'], 'Account created, check your email' )
		self.assertEqual(response.status_code, 201)

		response = self.client.post('/users/token/', {
			"email": "test@test.com", "password": "12345678"
		})
		
		self.assertEqual(response.status_code, 401)

	def test_confirm_password(self):
		user = User.objects.create_user("user", "user@email.com", "12345678")
		token = RefreshToken.for_user(user).access_token
		
		response = self.client.get("/users/verify-email/?token=" + str(token))
		
		self.assertEqual(response.data['message'], 'Account activated')
		self.assertEqual(response.status_code, 200)