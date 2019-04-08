import unittest # Importing the unittest module
from password import Password # Importing the password class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setup(self):
        '''
        Set up method to run before each test cases.
        '''