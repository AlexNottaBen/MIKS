#! /usr/bin/python3
# -*- coding: utf-8 -*-

from app import database


class ProductPhoto(database.Model):

    id = database.Column(database.Integer(), primary_key=True)
    url = database.Column(database.String(length=256), nullable=False)
    product_id = database.Column(
        database.Integer(), database.ForeignKey('product.id')
    )
