#! /usr/bin/python3
# -*- coding: utf-8 -*-

from IDeviceFactory import IDeviceFactory
from Device import OriginalRefurbishedDevice, ReplicaDevice


class OriginalRefurbishedDeviceFactory(IDeviceFactory):
    ''' A specific factory for original refurbished devices '''

    def create_device(self):
        # Implementation of creation of original devices
        return OriginalRefurbishedDevice()


class ReplicaDeviceFactory(IDeviceFactory):
    ''' A concrete factory for replicas from the Odessa basement '''

    def create_device(self):
        # Implementation of creation of replicas
        return ReplicaDevice()
