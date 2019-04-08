class Password:
    '''
    Class that generates new instances of passwords
    '''

    password_locker = []

    def __init__(self,user_name,pass_word):

        self.user_name = user_name
        self.pass_word = pass_word

    def save_password(self):
        '''
        save_password method saves password objects into password_locker
        '''

        Password.password_locker.append(self)    