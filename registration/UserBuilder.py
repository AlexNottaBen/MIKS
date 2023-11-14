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

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self._full_name = full_name

    @property
    def home_address(self):
        return self._home_address

    @home_address.setter
    def home_address(self, home_address: str):
        self._home_address = home_address

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        self._phone_number = phone_number

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        self._gender = gender

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number: str):
        self._card_number = card_number

    @property
    def cardholder_name(self):
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name: str):
        self._cardholder_name = cardholder_name

    @property
    def card_expire_month(self):
        return self._card_expire_month

    @card_expire_month.setter
    def card_expire_month(self, card_expire_month: str):
        self._card_expire_month = card_expire_month

    @property
    def card_expire_year(self):
        return self._card_expire_year

    @card_expire_year.setter
    def card_expire_year(self, card_expire_year: str):
        self._card_expire_year = card_expire_year


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
