#! /usr/bin/python3
# -*- coding: utf-8 -*-

from ICommand import ICommand


class EmergencyAnnouncementCommand(ICommand):
    """
    Specific command for emergency messages
    """

    def __init__(self, message):
        self.message = message

    def execute(self):
        print(f"Emergency Announcement: {self.message}")
