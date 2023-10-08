#! /usr/bin/python3
# -*- coding: utf-8 -*-

class User:
    ''' A class that describes a user '''

    def __init__(self, username: str, email: str, password: str, full_name: str, birthday: str, home_address: str, phone_number: str, gender: str, card_number: str, card_expire_month: str, card_expire_year: str, cardholder_name: str):
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.full_name: str = full_name
        self.birthday: str = birthday
        self.home_address: str = home_address
        self.phone_number: str = phone_number
        self.gender: str = gender
        self.card_number: str = card_number
        self.card_expire_month: str = card_expire_month
        self.card_expire_year: str = card_expire_year
        self.cardholder_name: str = cardholder_name

    def __str__(self) -> str:
        return f"\nКористувач: {self.username},\n- Пошта: {self.email},\n- Повне ім'я: {self.full_name},\n- Рік народження: {self.birthday},\n- Домашня адреса: {self.home_address},\n- Номер телефону: {self.phone_number}\n- Стать: {self.gender}\n- Картка: {self.cardholder_name} {self.card_number}, буде не дійсною {self.card_expire_month} {self.card_expire_year}\n"
