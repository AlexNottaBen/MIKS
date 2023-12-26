#! /usr/bin/python3
# -*- coding: utf-8 -*-

from typing import List


class SeasonalActionContext:
    """
    The context that defines when seasonal actions will be active
    """

    def __init__(self):
        self.active_bundles: List[str] = []

    def activate_bundle(self, bundle_name: str) -> None:
        self.active_bundles.append(bundle_name)

    def is_bundle_active(self, bundle_name: str) -> bool:
        return bundle_name in self.active_bundles
