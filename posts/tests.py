from django.test import TestCase

# Create your tests here.
class PostsTests(TestCase):
  def test_post_unauthed(self):
    response = self.client.post("/posts", {"title": "Test", "content": "Test"})
    self.assertEqual(response.status_code, 401)