from django.test import TestCase
from django.test import Client

# Create your tests here.
class UsersTests(TestCase):
  def test_create_user(self):
    c = Client()
    response = c.post("/users/", {
      "email": "test@test.com",
      "username": "test",
      "password": "12345678"
    })
    
    self.assertEqual(response.status_code, 201)