#! /usr/bin/python3
# -*- coding: utf-8 -*-

from Product import Product
from IAdditionalProducts import IAdditionalProducts


class AdditionalProducts(IAdditionalProducts):
    def get_same_type_products(self, type_of_product):
        """The logic of obtaining other products of the same type"""

        return Product.query.filter_by(type_of_product=type_of_product)

    def get_same_collection_products(self, collection):
        """The logic of obtaining other products from the same collection"""

        return Product.query.filter_by(collection=collection)
