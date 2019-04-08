#!/usr/bin/env python3.6 
from password import Password
    
def create_password(user_name,pass_word):
    '''
    Function to create a new password
    '''
    new_password = Password(user_name,pass_word)
    return new_password

def save_passwords(password):
    '''
     Function to save passwords
    '''
    password.save_password()

def del_password(password):
     '''
     Function to delete a contact
    '''
     password.delete_password()

def check_existing_passwords(user_name):
    '''
    Function that check if a password exists with that username and return a Boolean
    '''
    return Password.password_exist(user_name)

def display_passwords():
    '''
    Function that returns all the saved passwords
    '''
    return Password.display_passwords()

def main():
    print("Hello Welcome to your password locker.What is your name?")
       
      

  