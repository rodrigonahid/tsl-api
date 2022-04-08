from django.test import TestCase

from users.models import User
from rest_framework.test import APIClient

# Create your tests here.
class PostsTests(TestCase):
  def test_post_unauthorized(self):
    response = self.client.post("/posts/", {"title": "Test", "content": "Test"})
    self.assertEqual(response.status_code, 401)

  def test_post_authorized(self):
    user = User.objects.create_user("user", "user@email.com", "12345678")
    user.is_active = True
    user.save()

    response = self.client.post("/users/token/", {"email": "user@email.com", "password": "12345678"})
    
    token = response.data['access']

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    
    response = client.post(
      '/posts/',
      {"content": "Testing content"},
      format='json',
    )
    
    self.assertEqual(response.status_code, 201)

  def test_get_posts(self):
    response = self.client.get("/posts/")
    self.assertEqual(response.status_code, 200)
