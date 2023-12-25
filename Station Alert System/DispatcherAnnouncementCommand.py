#! /usr/bin/python3
# -*- coding: utf-8 -*-

from ICommand import ICommand


class DispatcherAnnouncementCommand(ICommand):
    """
    Specific command for dispatcher messages
    """

    def __init__(self, message):
        self.message = message

    def execute(self):
        print(f"Dispatcher Announcement: {self.message}")
