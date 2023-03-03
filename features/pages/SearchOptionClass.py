from selenium.webdriver.common.by import By
class SearchOptionClass:
    # Creating Element Locators
    def __init__(self, driver):
        self.driver = driver
        self.SearchBox ="//*[@placeholder='Search for your goal']"
        self.Subject = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]"

    # Creating Element Methods
    def click_SearchBox(self):
        SearchBox = self.driver.find_element(By.XPATH, self.SearchBox)
        SearchBox.click()
    def enter_coursename(self,cn):
        SearchBox = self.driver.find_element(By.XPATH, self.SearchBox)
        SearchBox.send_keys(cn)
    def enter_validcoursename(self,ivcn):
        SearchBox = self.driver.find_element(By.XPATH, self.SearchBox)
        SearchBox.send_keys(ivcn)
    def enter_invalidcoursename(self,vcn):
        SearchBox = self.driver.find_element(By.XPATH, self.SearchBox)
        SearchBox.send_keys(vcn)
    def click_subject(self):
        Subject = self.driver.find_element(By.XPATH, self.Subject)
        Subject.click()


















