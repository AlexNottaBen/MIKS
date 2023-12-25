#! /usr/bin/python3
# -*- coding: utf-8 -*-

from ICommand import ICommand


class MarketingAnnouncementCommand(ICommand):
    """
    Specific command for marketing messages
    """
    
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(f"Marketing Announcement: {self.message}")
