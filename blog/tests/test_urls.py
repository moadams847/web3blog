from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (PostListView, PostDetailView, PostCreateView, 
                        PostUpdateView, PostDeleteView, UserPostListView, CategoryListView, add_comment)

class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resovled(self):
        url = reverse('blog-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostListView)
        
    def test_detail_url_is_resovled(self):
        url = reverse('post-detail', args=[3])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
        
    def test_create_url_is_resovled(self):
        url = reverse('post-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_update_url_is_resovled(self):
        url = reverse('post-update', args=[3])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)
        
    def test_delete_url_is_resovled(self):
        url = reverse('post-delete', args=[3])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)
        
    def test_user_posts_url_is_resovled(self):
        url = reverse('user-posts', args=['user'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserPostListView)
        
    def test_category_posts_url_is_resovled(self):
        url = reverse('category-posts', args=['category'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CategoryListView)
        
    def test_add_comment_url_is_resovled(self):
        url = reverse('add-comment', args=[3])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_comment)
