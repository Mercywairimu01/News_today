import unittest
from app.models import news


# News = news.News

class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """
    
    def setup(self):
        '''
        Set up method that runs before each test
        '''
        self.news_source = news.News('CNN','CNN News','Cable News Newtork that is a leader in providing news worldwide','cnn.com','general','us')


    def test_instance(self):
        '''
        Test to check if new object it properly initialized
        '''
        self.assertTrue(isinstance(self.news_source,news))
       
       
if __name__ == '__main__':
    unittest.main()   