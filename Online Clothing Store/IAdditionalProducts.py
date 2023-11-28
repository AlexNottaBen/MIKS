#! /usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class IAdditionalProducts(ABC):
    @abstractmethod
    def get_same_type_products(self, product_type):
        pass

    @abstractmethod
    def get_same_collection_products(self, collection):
        pass
