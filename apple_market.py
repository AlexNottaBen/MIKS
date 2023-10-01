#! /usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from random import choice


class IDeviceFactory(ABC):
    ''' Інтерфейс абстрактної фабрики '''

    @abstractmethod
    def create_device(self):
        pass


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


class OriginalRefurbishedDevice:
    ''' Реалізація оригінального відновленого приладу '''
    
    def __str__(self) -> str:
        return "Оригінальний відновлений пристрій"


class ReplicaDevice:
    ''' Реалізація репліки з одеського підвалу '''
    
    def __str__(self) -> str:
        return "Репліка з одеського підвалу"


# Створення об'єкта фабрики на основі випадкового вибору
if choice([True, False]):
    factory = OriginalRefurbishedDeviceFactory()
else:
    factory = ReplicaDeviceFactory()

# Створення пристрою з використанням фабрики
device = factory.create_device()
print(f"Вибір: {device}")
