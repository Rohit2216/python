from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_post(self):
        url = reverse('post-list')
        data = {'username': 'testuser', 'caption': 'This is a test caption'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

    def test_view_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        post = Post.objects.create(username='testuser', caption='Test caption')
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
