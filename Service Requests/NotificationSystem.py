#! /usr/bin/python3
# -*- coding: utf-8 -*-


class NotificationSystem:
    def notify_client(self, client_address, notify) -> None:
        print("\nNotify for client", client_address, ":\n", notify)
