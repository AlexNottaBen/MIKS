#! /usr/bin/python3
# -*- coding: utf-8 -*-

from LoggingSystem import LoggingSystem
from NotificationSystem import NotificationSystem
from BrigadeAssignmentSystem import BrigadeAssignmentSystem


class TechnicalSupportFacade:
    def __init__(
        self,
        logging_system=LoggingSystem(),
        notification_system=NotificationSystem(),
        assignment_system=BrigadeAssignmentSystem(),
    ) -> None:
        self._logging_system: LoggingSystem = logging_system
        self._notification_system: NotificationSystem = notification_system
        self._assignment_system: BrigadeAssignmentSystem = assignment_system

    def open_service_request(self, client_address) -> None:
        print("\n*** Open Service Request ***")

        #  log the application in the system
        self._logging_system.log_request(client_address)

        # inform the client about the acceptance of the application
        self._notification_system.notify_client(
            client_address, "Your service request has been received."
        )

        # forward the client's address to a free team
        self._assignment_system.assign_brigade(client_address)

    def close_service_request(self, client_address) -> None:
        print("\n*** Close Service Request ***")

        # change the status in the magazine
        self._logging_system.update_status(client_address, "Closed")

        # send a letter to the client to evaluate the work
        self._notification_system.notify_client(
            client_address, "Please rate our service."
        )

        # transfer information about the completed application
        # to the accounting department
        self._assignment_system.notify_accounting(
            client_address, "Service request completed."
        )
