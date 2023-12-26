#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pygame.surface import Surface

from ICharacter import ICharacter


class Character(ICharacter):
    def __init__(self, sprite: Surface) -> None:
        self.position_x: int = 125
        self.position_y: int = 400
        self.jump_power: int = 10
        self.jump_count: int = self.jump_power
        self.sprite: Surface = sprite
        self.is_jump: bool = False
        self.current_bundle: str = "default"

    def accept(self, visitor):
        visitor.visit(self)

    def change_sprite(self, sprite: Surface) -> None:
        self.sprite = sprite

    def set_seasonal_bundle(self, bundle_name):
        self.current_bundle = bundle_name
