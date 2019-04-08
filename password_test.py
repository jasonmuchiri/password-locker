import unittest # Importing the unittest module
from password import Password # Importing the password class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("jasonmk","RJXP2I5") # create password object

    def test_init(self):
        '''
        test_init test case to rest if the object is initialized properly
        '''

        self.assertEqual(self.new_password.user_name,"jasonmk")
        self.assertEqual(self.new_password.pass_word,"RJXP2I5")
     