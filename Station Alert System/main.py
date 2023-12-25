#! /usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
from sys import argv

from eel import init, start, expose, sleep

from CommandQueue import CommandQueue
from AnnouncementPlayer import AnnouncementPlayer
from EmergencyAnnouncementCommand import EmergencyAnnouncementCommand
from DispatcherAnnouncementCommand import DispatcherAnnouncementCommand
from InformationAnnouncementCommand import InformationAnnouncementCommand
from MarketingAnnouncementCommand import MarketingAnnouncementCommand


def main() -> None:
    this_module_directory = path.dirname(path.abspath(argv[0]))

    init(path=f"{this_module_directory}/templates")

    start("index.html", mode="false", shutdown_delay=100000, port=5000)


@expose
def begin_simulation() -> None:
    print("Begin Simulation!")

    sleep(1.0)

    # Create command objects of various types
    emergency_command = EmergencyAnnouncementCommand(
        "Emergency situation! Evacuate immediately!"
    )
    info_command = InformationAnnouncementCommand(
        "Passenger announcement: John Doe, please come to the information desk."
    )
    dispatcher_command = DispatcherAnnouncementCommand(
        "Train arrival: Express train from City A."
    )
    marketing_command = MarketingAnnouncementCommand(
        "Special offer: Buy one, get one free!"
    )

    # Create an object for playing commands
    player = AnnouncementPlayer()

    # Reproduce the commands
    player.play(emergency_command)
    player.play(info_command)
    player.play(dispatcher_command)
    player.play(marketing_command)

    # Add commands to the queue and play the queue
    queue = CommandQueue()
    queue.add_command(emergency_command)
    queue.add_command(info_command)
    queue.add_command(info_command)
    queue.add_command(dispatcher_command)
    queue.add_command(dispatcher_command)
    queue.add_command(marketing_command)
    queue.add_command(emergency_command)
    queue.add_command(info_command)
    queue.add_command(emergency_command)
    queue.add_command(dispatcher_command)
    queue.add_command(marketing_command)
    queue.add_command(marketing_command)
    queue.process_commands()


if __name__ == "__main__":
    main()
