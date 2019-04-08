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

    def test_save_password(self):
        '''
        test_save_pasword test case to test if the password object is saved into the password locker
        '''
        self.new_password.save_password() # saving the new password
        self.assertEqual(len(Password.password_locker),1)

    def test_save_multiple_password(self):
        '''
        test_save_multiple_password to check if we can save multiple password
        objects to our password-locker
        '''
        self.new_password.save_password()
        test_password = Password("bongonati","W1E2E3D")
        test_password.save_password()
        self.assertEqual(len(Password.password_locker),2)

if __name__ == '__main__':
    unittest.main()        