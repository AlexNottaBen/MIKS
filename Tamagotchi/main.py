#! /usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
from sys import argv

import pygame
from pygame import *

from Character import Character


def main() -> None:
    this_module_directory = path.dirname(path.abspath(argv[0]))

    init()

    display.set_caption("Tamagotchi")

    screen_width, screen_height = (600, 800)

    screen = display.set_mode((screen_width, screen_height))

    screen.fill((0, 0, 0))

    character = Character(
        sprite=image.load(f"{this_module_directory}/assets/images/cat.png")
    )

    background = image.load(
        f"{this_module_directory}/assets/images/background.jpg"
    ).convert()

    clock = time.Clock()

    while True:
        clock.tick(30)  # set FPS
        mouse = pygame.mouse.get_pressed()

        if not character.is_jump:
            if mouse[0]:
                character.is_jump = True
        else:
            if character.jump_count >= -character.jump_power:
                if character.jump_count > 0:
                    character.position_y -= (character.jump_count**2) / 2
                    character.change_sprite(
                        sprite=image.load(f"{this_module_directory}/assets/images/cat_jump.png")
                    )
                else:
                    character.position_y += (character.jump_count**2) / 2
                    character.change_sprite(
                        sprite=image.load(f"{this_module_directory}/assets/images/cat_fall.png")
                    )
                character.jump_count -= 1
            else:
                character.change_sprite(
                    sprite=image.load(f"{this_module_directory}/assets/images/cat.png")
                )
                character.is_jump = False
                character.jump_count = character.jump_power

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background, (0, 0))
        screen.blit(character.sprite, (character.position_x, character.position_y))
        display.update()


if __name__ == "__main__":
    main()
