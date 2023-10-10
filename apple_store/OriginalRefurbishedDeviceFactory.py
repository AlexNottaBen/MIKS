#! /usr/bin/python3
# -*- coding: utf-8 -*-

from IDeviceFactory import IDeviceFactory
from OriginalRefurbishedDevice import OriginalRefurbishedDevice


class OriginalRefurbishedDeviceFactory(IDeviceFactory):
    ''' A specific factory for original refurbished devices '''

    def create_device(self):
        # Implementation of creation of original devices
        return OriginalRefurbishedDevice()
