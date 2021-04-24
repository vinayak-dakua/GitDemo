from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    namec = (By.ID, "country")
    ind = (By.LINK_TEXT, "India")
    tick = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    buy = (By.CSS_SELECTOR, "[value='Purchase']")
    mez = (By.CSS_SELECTOR, "[class='alert alert-success alert-dismissible']")


    # self.driver.find_element_by_id("country").send_keys("ind")
    def clickCountry(self):
        return self.driver.find_element(*ConfirmPage.namec)

    # self.driver.find_element_by_link_text("India").click()
    def clickInd(self):
        return self.driver.find_element(*ConfirmPage.ind)

    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    def tickCheckBox(self):
        return self.driver.find_element(*ConfirmPage.tick)

    # self.driver.find_element_by_css_selector("[value='Purchase']").click()
    def buyitem(self):
        return self.driver.find_element(*ConfirmPage.buy)

    # self.driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']")
    def getmessage(self):
        return self.driver.find_element(*ConfirmPage.mez)


