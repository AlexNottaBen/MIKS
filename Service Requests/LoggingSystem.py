#! /usr/bin/python3
# -*- coding: utf-8 -*-


class LoggingSystem:
    def log_request(self, client_address) -> None:
        print("\nRequest logged for client:", client_address)

    def update_status(self, client_address, status) -> None:
        print("\nStatus for client", client_address, "updated to", status)
