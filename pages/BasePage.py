from utilities import configReader
import logging
import allure

from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, page):
        self.page = page
