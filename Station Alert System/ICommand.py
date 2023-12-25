#! /usr/bin/python3
# -*- coding: utf-8 -*-

import eel

from abc import ABC, abstractmethod


class ICommand(ABC):
    """
    Command Interface
    """

    @eel.expose
    def execute(self) -> None:
        pass
