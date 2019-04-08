#!/usr/bin/env python3.6 
from password import Password

  def create-password(username,password):
      '''
      Function to create a new password
      '''
      new_password = Password(usename,password)
      return new_password

  def save_passwords(password):
      '''
      Function to save passwords
      '''
      password.save_password()