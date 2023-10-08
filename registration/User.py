#! /usr/bin/python3
# -*- coding: utf-8 -*-

class User:
    ''' Класс, що описує користувача '''
    
    def __init__(self, username, email, password, full_name, age, home_address):
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.full_name: str = full_name
        self.age: int = age
        self.home_address: str = home_address

    def __str__(self) -> str:
        return f"\nКористувач: {self.username},\n- Пошта: {self.email},\n- Повне ім'я: {self.full_name},\n- Вік: {self.age},\n- Домашня адреса: {self.home_address}\n"
