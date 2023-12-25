#! /usr/bin/python3
# -*- coding: utf-8 -*-


class CommandQueue:
    """
    Class for command queue
    """
    
    def __init__(self):
        self.queue = []

    def add_command(self, command):
        self.queue.append(command)

    def process_commands(self):
        for command in self.queue:
            command.execute()
