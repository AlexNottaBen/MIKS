#! /usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint

from eel import sleep


class CommandQueue:
    """
    Class for command queue
    """

    def __init__(self) -> None:
        self.queue = []

    def add_command(self, command) -> None:
        self.queue.append(command)

    def process_commands(self) -> None:
        for command in self.queue:
            sleep(randint(1, 3))
            command.execute()
