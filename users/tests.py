from django.test import TestCase

# Create your tests here.
class UsersTests(TestCase):
	def test_create_user(self):
		response = self.client.post("/users/", {
			"email": "test@test.com",
			"username": "test",
			"password": "12345678"
		})
		self.assertEqual(response.status_code, 201)

	def test_create_user_invalid_password(self):
			response = self.client.post("/users/", {
				"email": "test@test.com",
				"username": "test",
				"password": "123"
			})
			self.assertEqual(response.status_code, 400)

	def test_create_user_invalid_username(self):
			response = self.client.post("/users/", {
				"email": "test@test.com",
				"username": "test@* _dsa",
				"password": "123"
			})
			self.assertEqual(response.status_code, 400)		
			