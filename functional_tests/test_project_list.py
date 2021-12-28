from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from blog.models import Post, Category, Comment
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):
    
   def setUp(self):
       self.browser = webdriver.Chrome(ChromeDriverManager().install())
       
   def tearDown(self):
        self.browser.close()
        
   def test_no_project_list_is_displayed(self):
       self.browser.get(self.live_server_url)
       time.sleep(20)
       
