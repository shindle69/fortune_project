from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        #포스트목록을 가져온다
        response = self.client.get('/fortune_board/')  
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content,'html.parser')
        self.assertEqual(soup.title.text,'궁물쌤')

        navbar = soup.nav
        self.assertIn('게시판', soup.text) #navbar.text error 생김
        self.assertIn('About', soup.text)

        self.assertEqual(Post.objects.count(), 0)
        main_area = soup.find('div', id='main_area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        post_001 = Post.objects.create(
            title = '첫 번째 홈페이지 포스트입니다.',
            content = 'Hello World. Welcome to my world',
        )
        post_002 = Post.objects.create(
            title = '두 번째 홈페이지 포스트입니다.',
            content = 'Hello World2222222222. Welcome to my world',
        )
        self.assertEqual(Post.objects.count(), 2)

        response = self.client.get('/fortune_board/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content,'html.parser')
        main_area = soup.find('div', id='main_area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)



