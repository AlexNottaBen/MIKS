#! /usr/bin/python3
# -*- coding: utf-8 -*-


class LoggingSystem:
    def log_request(self, client_address) -> None:
        print("\nRequest logged for client:", client_address)


    def update_status(self, client_address, status) -> None:
        print("\nStatus for client", client_address, "updated to", status)


class NotificationSystem:
    def notify_client(self, client_address, notify) -> None:
        print("\nNotify for client", client_address, ":\n", notify)


class BrigadeAssignmentSystem:
    def notify_accounting(self, client_address, notify) -> None:
        print("\nNotify for accounting", client_address, ":\n", notify)


    def assign_brigade(self, client_address):
        print("\nAssign brigade for", client_address)


class TechnicalSupportFacade:
    def __init__(
        self, logging_system, notification_system, brigade_assignment_system
        ) -> None:

        self.logging_system: LoggingSystem = (
            logging_system
        )
        self.notification_system: NotificationSystem = (
            notification_system
        )
        self.brigade_assignment_system: BrigadeAssignmentSystem = (
            brigade_assignment_system
        )


    def open_service_request(self, client_address) -> None:
        #  log the application in the system
        self.logging_system.log_request(client_address)

        # inform the client about the acceptance of the application
        self.notification_system.notify_client(
            client_address, "Your service request has been received."
        )

        # forward the client's address to a free team
        self.brigade_assignment_system.assign_brigade(client_address)


    def close_service_request(self, client_address) -> None:
        # change the status in the magazine
        self.logging_system.update_status(client_address, "Closed")

        # send a letter to the client to evaluate the work
        self.notification_system.notify_client(
            client_address, "Please rate our service."
        )

        # transfer information about the completed application
        # to the accounting department
        self.brigade_assignment_system.notify_accounting(
            client_address, "Service request completed."
        )


def main():
    technica_support_facade = TechnicalSupportFacade(
        logging_system=LoggingSystem(),
        notification_system=NotificationSystem(),
        brigade_assignment_system=BrigadeAssignmentSystem()
    )
    technica_support_facade.open_service_request("212.45.33.64")
    technica_support_facade.close_service_request("212.45.33.64")


if __name__ == "__main__":
    main()
