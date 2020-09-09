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
        """ Test Error Cetak WO """
        noWo = [
            "WO.REG1-0000331", "WO.REG1-0000332", "WO.REG1-0000333",
            "WO.REG1-0000334", "WO.REG1-0000335", "WO.REG1-0000336",
            "WO.REG1-0000337", "WO.REG1-0000338", "WO.REG1-0000339",
            "WO.REG1-0000340", "WO.REG1-0000341", "WO.REG1-0000342",
            "WO.REG1-0000343", "WO.REG1-0000344", "WO.REG1-0000345",
            "WO.REG1-0000346", "WO.REG1-0000347", "WO.REG1-0000348",
            "WO.REG1-0000349", "WO.REG1-0000350", "WO.REG1-0000351",
            "WO.REG1-0000352", "WO.REG1-0000353", "WO.REG1-0000354",
            "WO.REG1-0000355", "WO.REG1-0000356", "WO.REG1-0000357",
            "WO.REG1-0000358", "WO.REG1-0000359", "WO.REG1-0000360",
            "WO.REG1-0000361", "WO.REG1-0000362", "WO.REG1-0000363",
            "WO.REG1-0000364", "WO.REG1-0000365", "WO.REG1-0000366",
            "WO.REG1-0000367", "WO.REG1-0000368", "WO.REG1-0000369",
            "WO.REG1-0000370", "WO.REG1-0000371", "WO.REG1-0000372",
            "WO.REG1-0000373", "WO.REG1-0000374", "WO.REG1-0000375",
            "WO.REG1-0000376", "WO.REG1-0000377", "WO.REG1-0000378",
            "WO.REG1-0000379", "WO.REG1-0000380", "WO.REG1-0000381",
            "WO.REG1-0000382", "WO.REG1-0000383", "WO.REG1-0000384",
            "WO.REG1-0000385", "WO.REG1-0000386", "WO.REG1-0000387",
            "WO.REG1-0000388", "WO.REG1-0000389", "WO.REG1-0000390",
            "WO.REG1-0000391", "WO.REG1-0000392", "WO.REG1-0000393",
            "WO.REG1-0000394", "WO.REG1-0000395", "WO.REG1-0000396",
            "WO.REG1-0000397", "WO.REG1-0000398", "WO.REG1-0000399",
            "WO.REG1-0000400", "WO.REG1-0000401", "WO.REG1-0000402",
            "WO.REG1-0000403", "WO.REG1-0000404", "WO.REG1-0000405",
            "WO.REG1-0000406", "WO.REG1-0000407", "WO.REG1-0000408",
            "WO.REG1-0000409", "WO.REG1-0000410", "WO.REG1-0000411",
            "WO.REG1-0000412", "WO.REG1-0000413", "WO.REG1-0000414",
            "WO.REG1-0000415", "WO.REG1-0000416", "WO.REG1-0000417",
            "WO.REG1-0000418", "WO.REG1-0000419", "WO.REG1-0000420",
            "WO.REG1-0000421", "WO.REG1-0000422", "WO.REG1-0000423",
            "WO.REG1-0000424", "WO.REG1-0000425", "WO.REG1-0000426",
            "WO.REG1-0000427", "WO.REG1-0000428", "WO.REG1-0000429",
            "WO.REG1-0000430", "WO.REG1-0000431", "WO.REG1-0000432",
            "WO.REG1-0000433", "WO.REG1-0000434", "WO.REG1-0000435",
            "WO.REG1-0000436", "WO.REG1-0000437", "WO.REG1-0000438",
            "WO.REG1-0000439", "WO.REG1-0000440", "WO.REG1-0000441",
            "WO.REG1-0000442", "WO.REG1-0000443", "WO.REG1-0000444",
            "WO.REG1-0000445", "WO.REG1-0000446", "WO.REG1-0000447",
            "WO.REG1-0000448", "WO.REG1-0000449", "WO.REG1-0000450",
            "WO.REG1-0000451", "WO.REG1-0000452", "WO.REG1-0000453",
            "WO.REG1-0000454", "WO.REG1-0000455", "WO.REG1-0000456",
            "WO.REG1-0000457", "WO.REG1-0000458", "WO.REG1-0000459",
            "WO.REG1-0000460", "WO.REG1-0000461", "WO.REG1-0000462",
            "WO.REG1-0000463", "WO.REG1-0000464", "WO.REG1-0000465",
            "WO.REG1-0000466", "WO.REG1-0000467", "WO.REG1-0000468",
            "WO.REG1-0000469", "WO.REG1-0000470", "WO.REG1-0000471",
            "WO.REG1-0000472", "WO.REG1-0000473", "WO.REG1-0000474",
            "WO.REG1-0000475", "WO.REG1-0000476", "WO.REG1-0000477",
            "WO.REG1-0000478", "WO.REG1-0000479", "WO.REG1-0000480",
            "WO.REG1-0000481", "WO.REG1-0000482", "WO.REG1-0000483",
            "WO.REG1-0000484", "WO.REG1-0000485", "WO.REG1-0000486",
            "WO.REG1-0000487", "WO.REG1-0000488", "WO.REG1-0000489",
            "WO.REG1-0000490", "WO.REG1-0000491", "WO.REG1-0000492",
            "WO.REG1-0000493", "WO.REG1-0000494", "WO.REG1-0000495",
            "WO.REG1-0000496", "WO.REG1-0000497", "WO.REG1-0000498",
            "WO.REG1-0000499", "WO.REG1-0000500", "WO.REG1-0000501",
            "WO.REG1-0000502", "WO.REG1-0000503", "WO.REG1-0000504",
            "WO.REG1-0000505", "WO.REG1-0000506", "WO.REG1-0000507",
            "WO.REG1-0000508", "WO.REG1-0000509", "WO.REG1-0000510",
            "WO.REG1-0000511", "WO.REG1-0000512", "WO.REG1-0000513",
            "WO.REG1-0000514", "WO.REG1-0000515", "WO.REG1-0000516",
            "WO.REG1-0000517", "WO.REG1-0000518", "WO.REG1-0000519",
            "WO.REG1-0000520", "WO.REG1-0000521", "WO.REG1-0000522",
            "WO.REG1-0000523", "WO.REG1-0000524", "WO.REG1-0000525",
            "WO.REG1-0000526", "WO.REG1-0000527", "WO.REG1-0000528",
            "WO.REG1-0000529", "WO.REG1-0000530", "WO.REG1-0000531",
            "WO.REG1-0000532", "WO.REG1-0000533", "WO.REG1-0000534",
            "WO.REG1-0000535", "WO.REG1-0000536", "WO.REG1-0000537",
            "WO.REG1-0000538", "WO.REG1-0000539", "WO.REG1-0000540",
            "WO.REG1-0000541", "WO.REG1-0000542", "WO.REG1-0000543",
            "WO.REG1-0000544", "WO.REG1-0000545", "WO.REG1-0000546",
            "WO.REG1-0000547", "WO.REG1-0000548", "WO.REG1-0000549",
            "WO.REG1-0000550", "WO.REG1-0000551", "WO.REG1-0000552",
            "WO.REG1-0000553", "WO.REG1-0000554", "WO.REG1-0000555",
            "WO.REG1-0000556", "WO.REG1-0000557", "WO.REG1-0000558",
            "WO.REG1-0000559", "WO.REG1-0000560", "WO.REG1-0000561",
            "WO.REG1-0000562", "WO.REG1-0000563", "WO.REG1-0000564",
            "WO.REG1-0000566", "WO.REG1-0000567", "WO.REG1-0000568",
            "WO.REG1-0000569", "WO.REG1-0000571", "WO.REG1-0000572",
            "WO.REG1-0000573", "WO.REG1-0000574", "WO.REG1-0000575",
            "WO.REG1-0000576", "WO.REG1-0000577", "WO.REG1-0000578",
            "WO.REG1-0000579", "WO.REG1-0000580", "WO.REG1-0000581",
            "WO.REG1-0000582", "WO.REG1-0000583", "WO.REG1-0000584",
            "WO.REG1-0000585", "WO.REG1-0000586", "WO.REG1-0000587",
            "WO.REG1-0000588", "WO.REG1-0000589", "WO.REG1-0000590",
            "WO.REG1-0000591", "WO.REG1-0000592", "WO.REG1-0000593",
            "WO.REG1-0000594", "WO.REG1-0000595", "WO.REG1-0000596",
            "WO.REG1-0000597", "WO.REG1-0000598", "WO.REG1-0000599",
            "WO.REG1-0000600", "WO.REG1-0000601", "WO.REG1-0000602",
            "WO.REG1-0000603", "WO.REG1-0000604", "WO.REG1-0000605",
            "WO.REG1-0000606", "WO.REG1-0000607", "WO.REG1-0000608",
            "WO.REG1-0000609", "WO.REG1-0000610", "WO.REG1-0000611",
            "WO.REG1-0000612", "WO.REG1-0000613", "WO.REG1-0000614",
            "WO.REG1-0000615", "WO.REG1-0000616", "WO.REG1-0000617",
            "WO.REG1-0000618", "WO.REG1-0000619", "WO.REG1-0000620",
            "WO.REG1-0000621", "WO.REG1-0000622", "WO.REG1-0000623",
            "WO.REG1-0000624", "WO.REG1-0000625", "WO.REG1-0000626",
            "WO.REG1-0000627", "WO.REG1-0000628", "WO.REG1-0000629",
            "WO.REG1-0000630", "WO.REG1-0000631", "WO.REG1-0000632",
            "WO.REG1-0000633", "WO.REG1-0000634", "WO.REG1-0000635",
            "WO.REG1-0000636", "WO.REG1-0000637", "WO.REG1-0000638",
            "WO.REG1-0000639", "WO.REG1-0000640", "WO.REG1-0000641",
            "WO.REG1-0000642", "WO.REG1-0000643", "WO.REG1-0000644",
            "WO.REG1-0000645", "WO.REG1-0000646", "WO.REG1-0000647",
            "WO.REG1-0000648", "WO.REG1-0000649", "WO.REG1-0000650",
            "WO.REG1-0000651", "WO.REG1-0000652", "WO.REG1-0000653",
            "WO.REG1-0000654", "WO.REG1-0000655", "WO.REG1-0000656",
            "WO.REG1-0000657", "WO.REG1-0000658", "WO.REG1-0000659",
            "WO.REG1-0000660", "WO.REG1-0000661", "WO.REG1-0000662",
            "WO.REG1-0000663", "WO.REG1-0000664", "WO.REG1-0000665",
            "WO.REG1-0000666", "WO.REG1-0000667", "WO.REG1-0000668",
            "WO.REG1-0000669", "WO.REG1-0000670", "WO.REG1-0000671",
            "WO.REG1-0000672", "WO.REG1-0000673", "WO.REG1-0000674",
            "WO.REG1-0000675", "WO.REG1-0000676", "WO.REG1-0000677",
            "WO.REG1-0000678", "WO.REG1-0000679", "WO.REG1-0000680",
            "WO.REG1-0000681", "WO.REG1-0000682", "WO.REG1-0000683",
            "WO.REG1-0000684", "WO.REG1-0000685", "WO.REG1-0000686",
            "WO.REG1-0000687", "WO.REG1-0000688", "WO.REG1-0000689",
            "WO.REG1-0000690", "WO.REG1-0000691", "WO.REG1-0000692",
            "WO.REG1-0000693", "WO.REG1-0000694", "WO.REG1-0000695",
            "WO.REG1-0000696", "WO.REG1-0000697", "WO.REG1-0000698",
            "WO.REG1-0000699", "WO.REG1-0000700", "WO.REG1-0000701",
            "WO.REG1-0000702", "WO.REG1-0000703", "WO.REG1-0000704",
            "WO.REG1-0000705", "WO.REG1-0000706", "WO.REG1-0000707",
            "WO.REG1-0000708", "WO.REG1-0000709", "WO.REG1-0000710",
            "WO.REG1-0000711", "WO.REG1-0000712", "WO.REG1-0000713",
            "WO.REG1-0000714", "WO.REG1-0000715", "WO.REG1-0000716",
            "WO.REG1-0000717", "WO.REG1-0000718", "WO.REG1-0000719",
            "WO.REG1-0000720", "WO.REG1-0000721", "WO.REG1-0000722",
            "WO.REG1-0000723", "WO.REG1-0000724", "WO.REG1-0000725",
            "WO.REG1-0000726", "WO.REG1-0000727", "WO.REG1-0000728",
            "WO.REG1-0000729", "WO.REG1-0000730", "WO.REG1-0000731",
            "WO.REG1-0000732", "WO.REG1-0000733", "WO.REG1-0000734",
            "WO.REG1-0000735", "WO.REG1-0000736", "WO.REG1-0000737",
            "WO.REG1-0000738", "WO.REG1-0000739", "WO.REG1-0000740",
            "WO.REG1-0000741", "WO.REG1-0000742", "WO.REG1-0000743",
            "WO.REG1-0000744", "WO.REG1-0000745", "WO.REG1-0000746",
            "WO.REG1-0000747", "WO.REG1-0000748", "WO.REG1-0000749",
            "WO.REG1-0000750", "WO.REG1-0000751", "WO.REG1-0000752",
            "WO.REG1-0000753", "WO.REG1-0000754", "WO.REG1-0000755",
            "WO.REG1-0000756", "WO.REG1-0000757", "WO.REG1-0000758",
            "WO.REG1-0000759", "WO.REG1-0000760", "WO.REG1-0000761",
            "WO.REG1-0000762", "WO.REG1-0000763", "WO.REG1-0000764",
            "WO.REG1-0000765", "WO.REG1-0000766", "WO.REG1-0000767",
            "WO.REG1-0000768", "WO.REG1-0000769", "WO.REG1-0000770",
            "WO.REG1-0000771", "WO.REG1-0000772", "WO.REG1-0000773",
            "WO.REG1-0000774", "WO.REG1-0000775", "WO.REG1-0000776",
            "WO.REG1-0000777", "WO.REG1-0000778", "WO.REG1-0000779",
            "WO.REG1-0000780", "WO.REG1-0000781", "WO.REG1-0000782",
            "WO.REG1-0000783", "WO.REG1-0000784", "WO.REG1-0000785",
            "WO.REG1-0000786", "WO.REG1-0000787", "WO.REG1-0000788",
            "WO.REG1-0000789", "WO.REG1-0000790", "WO.REG1-0000791",
            "WO.REG1-0000792", "WO.REG1-0000793", "WO.REG1-0000794",
            "WO.REG1-0000795", "WO.REG1-0000796", "WO.REG1-0000797",
            "WO.REG1-0000798", "WO.REG1-0000799", "WO.REG1-0000800",
            "WO.REG1-0000801", "WO.REG1-0000802", "WO.REG1-0000803",
            "WO.REG1-0000804", "WO.REG1-0000805", "WO.REG1-0000806",
            "WO.REG1-0000807", "WO.REG1-0000808", "WO.REG1-0000809",
            "WO.REG1-0000810", "WO.REG1-0000811", "WO.REG1-0000812",
            "WO.REG1-0000813", "WO.REG1-0000814", "WO.REG1-0000815",
            "WO.REG1-0000816", "WO.REG1-0000817", "WO.REG1-0000818",
            "WO.REG1-0000819", "WO.REG1-0000820", "WO.REG1-0000821",
            "WO.REG1-0000822", "WO.REG1-0000823", "WO.REG1-0000824",
            "WO.REG1-0000825", "WO.REG1-0000826", "WO.REG1-0000828",
            "WO.REG1-0000829", "WO.REG1-0000830", "WO.REG1-0000831",
            "WO.REG1-0000832", "WO.REG1-0000833", "WO.REG1-0000834",
            "WO.REG1-0000835", "WO.REG1-0000836", "WO.REG1-0000837",
            "WO.REG1-0000838", "WO.REG1-0000839", "WO.REG1-0000840",
            "WO.REG1-0000841", "WO.REG1-0000842", "WO.REG1-0000843",
            "WO.REG1-0000844", "WO.REG1-0000845", "WO.REG1-0000846",
            "WO.REG1-0000847", "WO.REG1-0000848", "WO.REG1-0000849",
            "WO.REG1-0000850", "WO.REG1-0000851", "WO.REG1-0000852",
            "WO.REG1-0000853", "WO.REG1-0000854", "WO.REG1-0000855",
            "WO.REG1-0000856", "WO.REG1-0000857", "WO.REG1-0000858",
            "WO.REG1-0000859", "WO.REG1-0000861", "WO.REG1-0000862",
            "WO.REG1-0000863", "WO.REG1-0000864", "WO.REG1-0000865",
            "WO.REG1-0000866", "WO.REG1-0000867", "WO.REG1-0000868",
            "WO.REG1-0000869", "WO.REG1-0000870", "WO.REG1-0000871",
            "WO.REG1-0000872", "WO.REG1-0000873", "WO.REG1-0000874",
            "WO.REG1-0000875", "WO.REG1-0000876", "WO.REG1-0000877",
            "WO.REG1-0000878", "WO.REG1-0000879", "WO.REG1-0000880",
            "WO.REG1-0000881", "WO.REG1-0000882", "WO.REG1-0000883",
            "WO.REG1-0000884", "WO.REG1-0000885", "WO.REG1-0000886",
            "WO.REG1-0000887", "WO.REG1-0000888", "WO.REG1-0000889",
            "WO.REG1-0000890", "WO.REG1-0000891", "WO.REG1-0000892",
            "WO.REG1-0000893", "WO.REG1-0000894", "WO.REG1-0000895",
            "WO.REG1-0000896", "WO.REG1-0000897", "WO.REG1-0000898",
            "WO.REG1-0000899", "WO.REG1-0000900", "WO.REG1-0000901",
            "WO.REG1-0000902", "WO.REG1-0000903", "WO.REG1-0000904",
            "WO.REG1-0000905", "WO.REG1-0000906", "WO.REG1-0000907",
            "WO.REG1-0000908", "WO.REG1-0000909", "WO.REG1-0000910",
            "WO.REG1-0000911", "WO.REG1-0000912", "WO.REG1-0000913",
            "WO.REG1-0000914", "WO.REG1-0000915", "WO.REG1-0000916",
            "WO.REG1-0000917", "WO.REG1-0000918", "WO.REG1-0000919",
            "WO.REG1-0000920", "WO.REG1-0000921", "WO.REG1-0000922",
            "WO.REG1-0000923", "WO.REG1-0000924", "WO.REG1-0000925",
            "WO.REG1-0000926", "WO.REG1-0000927", "WO.REG1-0000928",
            "WO.REG1-0000929", "WO.REG1-0000930", "WO.REG1-0000931",
            "WO.REG1-0000932", "WO.REG1-0000933", "WO.REG1-0000934",
            "WO.REG1-0000935", "WO.REG1-0000936", "WO.REG1-0000937",
            "WO.REG1-0000938", "WO.REG1-0000939", "WO.REG1-0000940",
            "WO.REG1-0000941", "WO.REG1-0000942", "WO.REG1-0000943",
            "WO.REG1-0000944", "WO.REG1-0000945", "WO.REG1-0000946",
            "WO.REG1-0000947", "WO.REG1-0000948", "WO.REG1-0000949",
            "WO.REG1-0000950", "WO.REG1-0000951", "WO.REG1-0000952",
            "WO.REG1-0000953", "WO.REG1-0000954", "WO.REG1-0000955",
            "WO.REG1-0000956", "WO.REG1-0000957", "WO.REG1-0000958",
            "WO.REG1-0000959", "WO.REG1-0000960", "WO.REG1-0000961",
            "WO.REG1-0000962", "WO.REG1-0000963", "WO.REG1-0000964",
            "WO.REG1-0000965", "WO.REG1-0000966", "WO.REG1-0000967",
            "WO.REG1-0000968", "WO.REG1-0000969", "WO.REG1-0000970",
            "WO.REG1-0000971", "WO.REG1-0000972", "WO.REG1-0000973",
            "WO.REG1-0000974", "WO.REG1-0000975", "WO.REG1-0000976",
            "WO.REG1-0000977", "WO.REG1-0000978", "WO.REG1-0000979",
            "WO.REG1-0000980", "WO.REG1-0000981", "WO.REG1-0000982",
            "WO.REG1-0000983", "WO.REG1-0000984", "WO.REG1-0000985",
            "WO.REG1-0000986", "WO.REG1-0000987", "WO.REG1-0000988",
            "WO.REG1-0000989", "WO.REG1-0000990", "WO.REG1-0000991",
            "WO.REG1-0000992", "WO.REG1-0000993", "WO.REG1-0000994",
            "WO.REG1-0000995", "WO.REG1-0000996", "WO.REG1-0000997",
            "WO.REG1-0000998", "WO.REG1-0000999", "WO.REG1-0001000",
            "WO.REG1-0001001", "WO.REG1-0001002", "WO.REG1-0001003",
            "WO.REG1-0001004", "WO.REG1-0001005", "WO.REG1-0001006",
            "WO.REG1-0001007", "WO.REG1-0001008", "WO.REG1-0001009"
        ]
        for x in noWo:
            baseUrl = "http://localhost/kumala/honda_sa_work_order/detail/"
            driver.get(baseUrl + x)
            driver.find_element_by_id("cetakwo").click()
            """ Get value """
            nama_customer1 = driver.find_element_by_id(
                "nama_customer").get_attribute("value")
            nama_customer = nama_customer1.split(" - ")
            alamat_stnk = driver.find_element_by_id(
                "alamat_stnk").get_attribute("value")
            no_polisi = driver.find_element_by_id("no_polisi").get_attribute(
                "value")
            no_rangka = driver.find_element_by_id("no_rangka").get_attribute(
                "value")

            driver.switch_to.window(driver.window_handles[1])
            html = driver.page_source
            findErroe = html.find("Notice")
            if findErroe != -1:
                print("error Notice {}".format(x))
            print(x)
            print("nama_customer: {} adalah : {}".format(
                html.find(nama_customer[0]), nama_customer))
            print("alamat_stnk: {} adalah : {}".format(html.find(alamat_stnk),
                                                       alamat_stnk))
            print("no_polisi: {} adalah : {}".format(html.find(no_polisi),
                                                     no_polisi))
            print("no_rangka: {} adalah : {}".format(html.find(no_rangka),
                                                     no_rangka))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])


if __name__ == "__main__":
    unittest.main()
