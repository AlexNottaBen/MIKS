#! /usr/bin/python3
# -*- coding: utf-8 -*-


class BrigadeAssignmentSystem:
    def notify_accounting(self, client_address, notify) -> None:
        print("\nNotify for accounting", client_address, ":\n", notify)

    def assign_brigade(self, client_address):
        print("\nAssign brigade for", client_address)
