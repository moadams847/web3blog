from django.test import TestCase, Client
from blog.models import Post, Category, Comment


class TestModels(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='General')
       
    def test_category_str(self):
        self.assertEqual(str(self.category), 'General')

    
    
   
