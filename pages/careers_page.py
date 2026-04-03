from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):

    SEE_ALL_TEAMS = (By.XPATH, "//a[contains(text(),'See all teams')]")
    QA_OPEN_POSITIONS = (By.XPATH, "//*[@id='open-roles']//*[contains(@data-department,'Quality Assurance')]//a[contains(text(),'5 Open Positions')]")

    def click_see_all_teams(self):
        self.driver.find_element(*self.SEE_ALL_TEAMS).click()

    def open_qa_positions(self):
        self.wait.until(self.EC.visibility_of_element_located(self.QA_OPEN_POSITIONS))
        self.driver.find_element(*self.QA_OPEN_POSITIONS).click()