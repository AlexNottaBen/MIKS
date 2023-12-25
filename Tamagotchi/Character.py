#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pygame.surface import Surface


class Character:
    def __init__(self, sprite: Surface) -> None:
        self.position_x: int = 125
        self.position_y: int = 400
        self.sprite: Surface = sprite
        self.jump_power: int = 10
        self.jump_count: int = self.jump_power
        self.is_jump = False

    def change_sprite(self, sprite: Surface) -> None:
        self.sprite = sprite
