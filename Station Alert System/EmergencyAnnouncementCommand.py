#! /usr/bin/python3
# -*- coding: utf-8 -*-

import eel

from ICommand import ICommand


class EmergencyAnnouncementCommand(ICommand):
    """
    Specific command for emergency messages
    """

    def __init__(self, message: str) -> None:
        self.message: str = message

    def execute(self) -> None:
        eel.append_emergency_alert(self.message)
