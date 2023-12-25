#! /usr/bin/python3
# -*- coding: utf-8 -*-

from ICommand import ICommand


class InformationAnnouncementCommand(ICommand):
    """
    Specific command for information messages
    """

    def __init__(self, message):
        self.message = message

    def execute(self):
        print(f"Information Announcement: {self.message}")
