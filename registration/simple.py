#! /usr/bin/python3
# -*- coding: utf-8 -*-

from UserBuilder import UserBuilder

# Create a user with all options
user1_builder = UserBuilder("tillman", "angeltillman@mail.org",
                    "gjherio5#@ajgerioh7",
                    birthday='2002-08-14')

user1_builder.full_name = "Angel Tillman"
user1_builder.home_address = "023 Hailie Forges"
user1_builder.phone_number = "0506456845"
user1_builder.gender = "male"
user1_builder.card_number = "9684757478354324"
user1_builder.cardholder_name = "Angel Tillman"
user1_builder.card_expire_month = "july"
user1_builder.card_expire_year = "2024"

user1 = user1_builder.build()

print(user1)

# Creating a user with mandatory parameters
user2_builder = UserBuilder("alia", "alia@mail.org",
                    "yk5-kuprkfg[434]34hfg",
                    '2001-06-12'
                    )

user2 = user2_builder.build()

print(user2)
