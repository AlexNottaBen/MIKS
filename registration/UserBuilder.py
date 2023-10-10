#! /usr/bin/python3
# -*- coding: utf-8 -*-

from User import User

class UserBuilder:
    ''' Builder of user. '''
    
    def __init__(self, username: str,
                 email: str,
                 password: str,
                 birthday: str
                 ):
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.full_name: str = ''
        self.birthday: str = birthday
        self.home_address: str = ''
        self.phone_number: str = ''
        self.gender: str = 'not mention'
        self.card_number: str = ''
        self.card_expire_month: str = ''
        self.card_expire_year: str = ''
        self.cardholder_name: str = ''

    def set_full_name(self, full_name: str):
        self.full_name = full_name
        return self

    def set_home_address(self, home_address: str):
        self.home_address = home_address
        return self

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number
        return self

    def set_gender(self, gender: str):
        self.gender = gender
        return self

    def set_card_number(self, card_number: str):
        self.card_number = card_number
        return self

    def set_cardholder_name(self, cardholder_name: str):
        self.cardholder_name = cardholder_name
        return self

    def set_card_expire_month(self, card_expire_month: str):
        self.card_expire_month = card_expire_month
        return self
    
    def set_card_expire_year(self, card_expire_year: str):
        self.card_expire_year = card_expire_year
        return self

    def build(self) -> User:
        return User(
            self.username,
            self.email,
            self.password,
            self.full_name,
            self.birthday,
            self.home_address,
            self.phone_number,
            self.gender,
            self.card_number,
            self.card_expire_month,
            self.card_expire_year,
            self.cardholder_name
            )
