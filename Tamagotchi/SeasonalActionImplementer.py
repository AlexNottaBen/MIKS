#! /usr/bin/python3
# -*- coding: utf-8 -*-

from Character import Character
from SeasonalActionVisitor import SeasonalActionVisitor


class SeasonalActionImplementer(SeasonalActionVisitor):
    """
    Specific Visitor
    """

    def visit(self, character: Character) -> None:
        character.set_seasonal_bundle("xmas")
