#! /usr/bin/python3
# -*- coding: utf-8 -*-

from UserBuilder import UserBuilder

# Створення користувача зі всіма параметрами
user1 = UserBuilder("tillman", "angeltillman@mail.org", "gjherio5#@ajgerioh7", birthday='2002-08-14') \
    .set_full_name("Angel Tillman") \
    .set_home_address("023 Hailie Forges") \
    .set_phone_number("0506456845") \
    .set_gender("чоловік") \
    .set_card_number("9684757478354324") \
    .set_cardholder_name("Angel Tillman") \
    .set_card_expire_month("july") \
    .set_card_expire_year("2024") \
    .build()

print(user1)

# Створення користувача з обов'язковими параметрами
user2 = UserBuilder("alia", "alia@mail.org", "yk5-kuprkfg[434]34hfg", '2001-06-12').build()

print(user2)
