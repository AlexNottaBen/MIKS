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


# Створення користувача зі всіма параметрами
user1 = UserBuilder("tillman", "angeltillman@mail.org", "gjherio5#@ajgerioh7") \
    .set_full_name("Angel Tillman") \
    .set_age(29) \
    .set_home_address("023 Hailie Forges") \
    .build()

print(user1)

# Створення користувача з обов'язковими параметрами
user2 = UserBuilder("alia", "alia@mail.org", "yk5-kuprkfg[434]34hfg").build()

print(user2)
