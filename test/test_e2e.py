import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()

        for product in cards:
            productName = product.find_element_by_xpath("div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()

        checkOutPage.clickCheckOutBtn().click()
        confirmPage = checkOutPage.clickSuccessBtn()
        log.info("Entering country name as ind")
        confirmPage.clickCountry().send_keys("ind")
        self.verifyLinkTest("India")
        confirmPage.clickInd().click()
        confirmPage.tickCheckBox().click()
        confirmPage.buyitem().click()
        message = confirmPage.getmessage().text
        log.info("Test from application "+message)
        assert "Success!" in message
        self.driver.get_screenshot_as_file("sereen.png")

        print("add by gitDemo first time")
        print("add by gitDemo second time")
        print("add 3rd time")
        print("This is done by GitX")
        print("this is done by GitDemo in develop ")
        print("this is by gitx devlop 1st time")






