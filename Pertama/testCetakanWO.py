# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import unittest, time, re


class TestingUsePython(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            '/opt/lampp/htdocs/selenium_test/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case(self):
        """ Test Login """
        driver = self.driver
        driver.get("http://localhost/kumala/honda")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("0402109")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("birakomputer")
        driver.find_element_by_id("submit").click()
        """ Test Cetak WO """
        noWo = ["WO.REG1-0005665", "WO.REG1-0005666", "WO.REG1-0005662"]
        for x in noWo:
            baseUrl = "http://localhost/kumala/honda_sa_work_order/detail/"
            driver.get(baseUrl + x)


if __name__ == "__main__":
    unittest.main()
