#! /usr/bin/python3
# -*- coding: utf-8 -*-

from UserBuilder import UserBuilder

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
