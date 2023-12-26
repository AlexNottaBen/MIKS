#! /usr/bin/python3
# -*- coding: utf-8 -*-

import eel

from ICommand import ICommand


class InformationAnnouncementCommand(ICommand):
    """
    Specific command for information messages
    """

    def __init__(self, message: str) -> None:
        self.message: str = message

    def execute(self) -> None:
        eel.append_information_alert(self.message)
