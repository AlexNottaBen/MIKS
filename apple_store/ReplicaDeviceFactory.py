#! /usr/bin/python3
# -*- coding: utf-8 -*-

from IDeviceFactory import IDeviceFactory
from ReplicaDevice import ReplicaDevice


class ReplicaDeviceFactory(IDeviceFactory):
    ''' A concrete factory for replicas from the Odessa basement '''

    def create_device(self):
        # Implementation of creation of replicas
        return ReplicaDevice()
