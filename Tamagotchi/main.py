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

    label = font.Font(
        f"{this_module_directory}/assets/font/Kingthings Christmas 2.2.ttf", 40
    )
    xmasbundle_button = label.render("Get Christmas Bundle", True, (255, 0, 0))
    xmasbundle_button_collisionshape = xmasbundle_button.get_rect(topleft=(300, 300))

    character = Character(
        sprite=image.load(f"{this_module_directory}/assets/images/cat_default.png")
    )

    special_window = image.load(
        f"{this_module_directory}/assets/images/special_window.png"
    )
    is_show_special_window: bool = False

    background_type = "default"

    clock = time.Clock()

    while True:
        background = image.load(
            f"{this_module_directory}/assets/images/background_{background_type}.jpg"
        ).convert()
        clock.tick(30)  # set FPS
        mouse = pygame.mouse.get_pressed()
        mouse_positions = pygame.mouse.get_pos()

        if mouse_positions[0] < 400 and mouse_positions[1] < 100 and mouse[0]:
            is_show_special_window = True

        elif is_show_special_window and mouse[0]:
            is_show_special_window = False
            xmasbundle_button.set_alpha(1)
            character.change_suit("xmas")
            background_type = "xmas"

        if not character.is_jump:
            if mouse[0]:
                character.is_jump = True
        else:
            if character.jump_count >= -character.jump_power:
                if character.jump_count > 0:
                    character.position_y -= (character.jump_count**2) / 2
                    character.change_sprite(
                        sprite=image.load(
                            f"{this_module_directory}/assets/images/cat_jump_{character.suit}.png"
                        )
                    )
                else:
                    character.position_y += (character.jump_count**2) / 2
                    character.change_sprite(
                        sprite=image.load(
                            f"{this_module_directory}/assets/images/cat_fall_{character.suit}.png"
                        )
                    )
                character.jump_count -= 1
            else:
                character.change_sprite(
                    sprite=image.load(
                        f"{this_module_directory}/assets/images/cat_{character.suit}.png"
                    )
                )
                character.is_jump = False
                character.jump_count = character.jump_power

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background, (0, 0))
        screen.blit(character.sprite, (character.position_x, character.position_y))

        screen.blit(xmasbundle_button, (0, 0))

        if is_show_special_window:
            screen.blit(special_window, (20, 100))

        display.update()


if __name__ == "__main__":
    main()
