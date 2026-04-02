from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):

    SEE_ALL_TEAMS = (By.XPATH, "//a[contains(text(),'See all teams')]")
    QA_TEAM = (By.XPATH, "//h3[contains(text(),'Quality Assurance')]")

    def click_see_all_teams(self):
        self.driver.find_element(*self.SEE_ALL_TEAMS).click()

    def open_qa_positions(self):
        self.driver.find_element(*self.QA_TEAM).click()