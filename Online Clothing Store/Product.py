#! /usr/bin/python3
# -*- coding: utf-8 -*-

from app import database


class Product(database.Model):

    id = database.Column(database.Integer(), primary_key=True)
    name = database.Column(database.String(length=64), nullable=False)
    price = database.Column(database.Integer(), nullable=False)
    description = database.Column(database.Text(), nullable=False)
    type_of_product = database.Column(database.String(length=64), nullable=True)
    collection = database.Column(database.String(length=64), nullable=True)
    # 1 product can have inf photos. Invisible in SQlite
    photos = database.relationship('ProductPhoto', lazy=True)
    brand = database.Column(database.String(length=64), nullable=True)
    product_code = database.Column(database.String(length=64), nullable=True)
    availability = database.Column(database.String(length=64), nullable=True)
