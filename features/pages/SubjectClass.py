from selenium.webdriver.common.by import By
class SubjectClass:
    # Creating Element Locators
    def __init__(self, driver):
        self.driver = driver
        self.FullStack = "//*[text()='Get started']"
        #self.FullStack = "//h1[@class='css-p9q63i-H1-Title e1k53atl9']"

    def click_FullStack(self):
        FullStack = self.driver.find_element(By.XPATH, self.FullStack)
        FullStack.click()

