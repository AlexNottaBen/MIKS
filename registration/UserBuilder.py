#! /usr/bin/python3
# -*- coding: utf-8 -*-

from User import User

class UserBuilder:
    ''' Будівельник користувача. '''
    
    def __init__(self, username, email, password):
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.full_name: str = None
        self.age: int = None
        self.home_address: str = None

    def set_full_name(self, full_name):
        self.full_name = full_name
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_home_address(self, home_address):
        self.home_address = home_address
        return self

    def build(self) -> User:
        return User(self.username, self.email, self.password, self.full_name, self.age, self.home_address)
