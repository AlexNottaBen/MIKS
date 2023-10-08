#! /usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class IDeviceFactory(ABC):
    ''' Abstract factory interface '''

    @abstractmethod
    def create_device(self):
        pass
