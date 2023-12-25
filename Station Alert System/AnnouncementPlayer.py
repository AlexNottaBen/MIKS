#! /usr/bin/python3
# -*- coding: utf-8 -*-


class AnnouncementPlayer:
    """
    A class for playing commands through a loudspeaker system
    """

    def play(self, command):
        command.execute()
