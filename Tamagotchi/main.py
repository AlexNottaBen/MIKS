#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame import *


def main() -> None:

    init()

    display.set_caption("Tamagotchi")

    screen_width, screen_height = (600, 800)

    screen = display.set_mode((screen_width, screen_height))

    screen.fill((0, 0, 0))

    background = image.load("./Tamagotchi/assets/images/background.jpg").convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(background, (0, 0))
        display.update()


if __name__ == "__main__":
    main()
