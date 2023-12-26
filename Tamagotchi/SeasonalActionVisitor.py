#! /usr/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class SeasonalActionVisitor(ABC):
    """
    Visitor for Seasonal Activities
    """

    @abstractmethod
    def visit(self, character: "Character") -> None:
        pass
