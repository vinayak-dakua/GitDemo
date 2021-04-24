from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    checkOutBtn = (By.CSS_SELECTOR, "[class='nav-link btn btn-primary']")
    successBtn = (By.CSS_SELECTOR, "[class*='btn-success']")

    # driver.find_elements_by_xpath("//div[@class='card h-100']")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    # driver.find_element_by_css_selector("[class='nav-link btn btn-primary']").click()
    def clickCheckOutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtn)

    # self.driver.find_element_by_css_selector("[class*='btn-success']").click()
    def clickSuccessBtn(self):
        self.driver.find_element(*CheckOutPage.successBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

