# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# browser = webdriver.Chrome('/opt/lampp/htdocs/selenium_test/chromedriver')  # lokasi file chromedriver.exe
# Login username
# browser.get("http://localhost/kumala/honda_cco_customer_service/tambah")
# browser.get("http://localhost/kumala/honda_sa_work_order/detail/WO.REG1-0005665")
# browser.find_element_by_id("username").send_keys("0402109")
# browser.find_element_by_id("password").send_keys("birakomputer")
# browser.find_element_by_name("submit").click()
# select = Select(driver.find_element_by_id('pilih_regional'))
# select.select_by_visible_text('MANADO | Jl. Raya Manado - Tomohon KM7 Winangun Atas')

# browser.find_element_by_id("no_rangka").click()
# browser.find_element_by_id("no_rangka").clear()
# browser.find_element_by_id("no_rangka").send_keys("12")
# browser.find_element_by_xpath("//div[10]/div[8]").click()
# browser.find_element_by_id("generate").click()
# browser.find_element_by_id("simpan").click()

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            '/opt/lampp/htdocs/selenium_test/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/kumala/honda")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("0402109")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("birakomputer")
        driver.find_element_by_name("submit").click()
        var = "http://localhost/kumala/honda_sa_work_order/detail/"
        textQc = "QC PASSED By Andi Chaerul "
        for i in no_wo:
            ix = i
            driver.get(var + i)
            jasa = driver.find_element_by_id("total_biaya_jasa").text
            jasa_int = jasa.replace(".","")
            part = driver.find_element_by_id("total_biaya_part").text
            part_int = part.replace(".","")
            lain = driver.find_element_by_id("total_biaya_lain").text
            lain_int = lain.replace(".","")
            sub_total = driver.find_element_by_id("sub_total").text
            sub_total_int = sub_total.replace(".","")
            jumlahkan = jasa_int + part_int + lain_int
            if jumlahkan != sub_total_int:
                print(ix)
            else:
                print(textQc + ix)    


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
