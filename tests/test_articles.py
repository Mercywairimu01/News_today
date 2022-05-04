import unittest
from app.models import Articles



class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviour of articles class
    '''
    def setUp(self):
        '''
        Set up method that runs before each test
        '''
        self.new_article = Articles(id,'Greg Kumparak', "Elon's big week","TechCrunch Week in Review welcomes its new host, Greg Kumparak", "https://techcrunch.com/2022/04/30/elons-big-week/", "https://techcrunch.com/wp-content/uploads/2019/07/DSCF2578.jpg?w=600","2022-04-30T20:00:22Z","Hi!\r\nI’m Greg Kumparak.\r\nI’ll be heading up Week in Review for the foreseeable future, with your former host Lucas Matney diving into cryptoland with the launch of a newsletter and podcast called Cha… [+4576 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
        
if __name__ == '__main__':
    unittest.main()