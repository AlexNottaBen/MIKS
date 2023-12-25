#! /usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class ICommand(ABC):
    """
    Command Interface
    """
    
    @abstractmethod
    def execute(self):
        pass
