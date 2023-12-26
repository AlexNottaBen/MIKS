#! /usr/bin/python3
# -*- coding: utf-8 -*-

import eel

from ICommand import ICommand


class MarketingAnnouncementCommand(ICommand):
    """
    Specific command for marketing messages
    """

    def __init__(self, message: str) -> None:
        self.message: str = message

    def execute(self) -> None:
        eel.append_marketing_alert(self.message)
