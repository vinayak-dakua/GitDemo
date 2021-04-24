from selenium.webdriver.common.by import By
from pageObject.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    mf = (By.ID, "exampleFormControlSelect1")
    tick = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    msz = (By.CLASS_NAME, "alert-success")

    # driver.find_element_by_css_selector("a[href*='shop']").
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    # driver.find_element_by_css_selector("input[name='name']").send_keys("Vinayak")
    def enterName(self):
        return self.driver.find_element(*HomePage.name)

    # driver.find_element_by_name("email").send_keys("vinayak@gmail.com")
    def enteremail(self):
        return self.driver.find_element(*HomePage.email)

    # driver.find_element_by_name("email").send_keys("vinayak@gmail.com")
    def mOrF(self):
        return self.driver.find_element(*HomePage.mf)

    # driver.find_element_by_id("exampleCheck1").click()
    def clickTick(self):
        return self.driver.find_element(*HomePage.tick)

    # driver.find_element_by_xpath("//input[@type='submit']").click()
    def submitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    # message = driver.find_element_by_class_name("alert-success").text
    def getMsz(self):
        return self.driver.find_element(*HomePage.msz)





