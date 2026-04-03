import re

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class QAPage(BasePage):

    JOB_LIST = (By.XPATH, "//*[@data-qa='posting-name']")
    JOB_LOCATION_LIST = (By.XPATH, "//*[contains(@aria-label,'Location:')]//a[contains(@class,'category-link')]")
    JOB_DEPARTMENT_LIST = (By.XPATH, "//*[contains(@aria-label,'Filter by Team:')]//a[contains(@class,'category-link')]")
    APPLY_BUTTON = (By.XPATH, "//a[contains(text(),'Apply')]")

    def get_jobs(self):
        return self.driver.find_elements(*self.JOB_LIST)

    def get_job_locations(self):
        return self.driver.find_elements(*self.JOB_LOCATION_LIST)

    def get_job_departments(self):
        return self.driver.find_elements(*self.JOB_DEPARTMENT_LIST)

    def validate_jobs(self):
        jobs_elements = self.get_jobs()
        assert len(jobs_elements) > 0, "No jobs found"
        jobs_list = [job.text for job in jobs_elements]
    def validate_jobs(self):
        jobs_elements = self.get_jobs()
        assert len(jobs_elements) > 0, "No jobs found"
        jobs_list = [job.text for job in jobs_elements]
        non_matching_jobs = [job for job in jobs_list if "Quality Assurance" not in job]

        assert not non_matching_jobs, f"Not all jobs contain 'Quality Assurance'. Non-matching jobs: {non_matching_jobs}"

    def validate_locations(self):
        location_elements = self.get_job_locations()
        assert len(location_elements) > 0, "No job locations found"
        location_list = [loc.get_attribute("text") for loc in location_elements]

        assert "Istanbul, Turkey" in location_list, "'Istanbul, Turkey' is not in the job locations"

    def validate_departments(self):
        department_elements = self.get_job_departments()
        assert len(department_elements) > 0, "No job departments found"
        department_list = [dept.get_attribute("text") for dept in department_elements]

        assert "Quality Assurance" in department_list, "'Quality Assurance' is not in the job departments"

    def click_apply(self):
        self.driver.find_element(*self.APPLY_BUTTON).click()

    def is_redirected_to_lever(self):
        expected_url_prefix = "https://jobs.lever.co/insiderone/"
        current_url = self.driver.current_url
        assert current_url.startswith(expected_url_prefix)

        # Validate UUID-like job ID
        pattern = r"https://jobs\.lever\.co/insiderone/[a-f0-9\-]+"
        assert re.match(pattern, current_url) is not None, "Current URL does not match the expected pattern for Lever job postings"