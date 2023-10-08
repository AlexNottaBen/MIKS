#! /usr/bin/python3
# -*- coding: utf-8 -*-

from IDeviceFactory import IDeviceFactory
from Device import OriginalRefurbishedDevice, ReplicaDevice

class OriginalRefurbishedDeviceFactory(IDeviceFactory):
    ''' Конкретна фабрика для оригінальних відновлених пристроїв '''

    def create_device(self):
        # Реалізація створення оригінальних пристроїв
        return OriginalRefurbishedDevice()


class ReplicaDeviceFactory(IDeviceFactory):
    ''' Конкретна фабрика для реплік з одеського підвалу '''

    def create_device(self):
        # Реалізація створення реплік
        return ReplicaDevice()