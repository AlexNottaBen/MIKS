#! /usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class ICharacter(ABC):
    """
    Base Character Class
    """

    @abstractmethod
    def accept(self, visitor) -> None:
        pass
