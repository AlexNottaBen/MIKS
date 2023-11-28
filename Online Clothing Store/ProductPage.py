#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template

from IAdditionalProducts import IAdditionalProducts


class ProductPage:
    def __init__(self, additional_products: IAdditionalProducts):
        self._additional_products = additional_products

    def show_additional_products(self, product, photos):
        same_type_products = (
            self._additional_products.get_same_type_products(
                type_of_product=product.type_of_product
            )
        )
        same_collection_products = (
            self._additional_products.get_same_collection_products(
                collection=product.collection
            )
        )

        # The logic of displaying additional products on the page
        return render_template(
            "product.html",
            product=product,
            photos=photos,
            same_type_products=same_type_products,
            same_collection_products=same_collection_products,
        )
