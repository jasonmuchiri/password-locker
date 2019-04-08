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
    print("Hello Welcome to your password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cp - create a new password, dp - display passwords, ex - exit the password locker ")
        short_code = input().lower()
        if short_code == 'cp':
            print("New Password")
            print("-"*10)

            print("Username ...")
            user_name = input()

            print("Password ...")
            pass_word = input()

            save_passwords(create_password(user_name,pass_word))
            print('\n')
            print(f"New Password {user_name} {pass_word} created")
            print ('\n')

        elif short_code == 'dp':
            if display_passwords():
                print("Here is a list of all your passwords")
                print('\n')
                for password in display_passwords():
                    print(f"{password.user_name} {password.pass_word}")
                print('\n')
            else:
                print('\n')
                print("You don't seem to have any passwords saved yet")
                print('\n')
        elif short_code == "ex":
            print("Bye .....")
            break
        else:
            print("I really didn't get that. Please use the short codes")                                                
