import unittest
from app.models import News


# News = news.News

class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """
    
    def setUp(self):
        '''
        Set up method that runs before each test
        '''
        self.news_source = News('CNN','CNN News','Cable News Newtork that is a leader in providing news worldwide','cnn.com','general','us')


    def test_instance(self):
        '''
        Test to check if new object it properly initialized
        '''
        self.assertTrue(isinstance(self.news_source,News))
       
       
if __name__ == '__main__':
    unittest.main()   