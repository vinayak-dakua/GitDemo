from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):

    def test_formSubmittion(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.enterName().send_keys(getData["firstname"])
        log.info("firstname"+getData["firstname"] )
        homePage.enteremail().send_keys(getData["email"])
        # Select class provided some method to handle dropdown
        self.selectOptionByText(homePage.mOrF(), getData["gender"])
        homePage.clickTick().click()
        homePage.submitBtn().click()
        message = homePage.getMsz().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

