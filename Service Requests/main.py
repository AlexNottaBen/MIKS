#! /usr/bin/python3
# -*- coding: utf-8 -*-

from TechnicalSupportFacade import TechnicalSupportFacade


def main():
    technica_support_facade: TechnicalSupportFacade = TechnicalSupportFacade()
    technica_support_facade.open_service_request("212.45.33.64")
    technica_support_facade.close_service_request("212.45.33.64")


if __name__ == "__main__":
    main()
