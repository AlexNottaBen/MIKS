#! /usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class AdditionalItemsImplementation(ABC):
    @abstractmethod
    def get_same_type_items(self, product_type):
        pass

    @abstractmethod
    def get_same_collection_items(self, collection):
        pass


class AdditionalItemsImplementationConcrete(AdditionalItemsImplementation):
    def get_same_type_items(self, product_type):
        print("The logic of obtaining other goods of the same type")

    def get_same_collection_items(self, collection):
        print("The logic of obtaining other products from the same collection")


class ProductPage:
    def __init__(self, additional_items_implementation: AdditionalItemsImplementation):
        self._additional_items_implementation = additional_items_implementation

    def show_additional_items(self, product_type, collection):
        same_type_items = self._additional_items_implementation.get_same_type_items(
            product_type
        )
        same_collection_items = (
            self._additional_items_implementation.get_same_collection_items(collection)
        )

        print("The logic of displaying additional products on the page")


additional_items_implementation = AdditionalItemsImplementationConcrete()
product_page = ProductPage(additional_items_implementation)

product_type = ""
collection = ""

# Call the function to display additional products
product_page.show_additional_items(product_type, collection)
