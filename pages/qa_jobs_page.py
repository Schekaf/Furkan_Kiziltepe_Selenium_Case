from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class QAPage(BasePage):

    JOB_LIST = (By.CSS_SELECTOR, ".position-list-item")
    APPLY_BUTTON = (By.XPATH, "//a[contains(text(),'Apply')]")

    def get_jobs(self):
        return self.driver.find_elements(*self.JOB_LIST)

    def validate_jobs(self):
        jobs = self.get_jobs()
        assert len(jobs) > 0, "No jobs found"

        for job in jobs:
            text = job.text
            assert "Quality Assurance" in text
            assert "Istanbul" in text

    def click_apply(self):
        self.driver.find_element(*self.APPLY_BUTTON).click()

    def is_redirected_to_lever(self):
        return "lever.co" in self.driver.current_url