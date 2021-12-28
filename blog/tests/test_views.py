from django.test import TestCase, Client
from django.urls import reverse, resolve
from blog.models import Post, Category, Comment
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('blog-home')
        self.detail_url = reverse('post-detail', kwargs={'pk': 9})

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
    
        
         
    