#! /usr/bin/python3
# -*- coding: utf-8 -*-

import eel

from ICommand import ICommand


class DispatcherAnnouncementCommand(ICommand):
    """
    Specific command for dispatcher messages
    """

    def __init__(self, message: str) -> None:
        self.message: str = message

    def execute(self) -> None:
        eel.append_dispatcher_alert(self.message)
