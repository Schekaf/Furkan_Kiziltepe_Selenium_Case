from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class QAPage(BasePage):

    JOB_LIST = (By.XPATH, "//*[@data-qa='posting-name']")
    JOB_LOCATION_LIST = (By.XPATH, "//*[contains(@aria-label,'Location:')]//a[contains(@class,'category-link')]")
    JOB_DEPARTMENT_LIST = (By.XPATH, "//*[contains(@aria-label,'Filter by Team:')]//a[contains(@class,'category-link')]")
    APPLY_BUTTON = (By.XPATH, "//a[contains(text(),'Apply')]")
    APPLY_FOR_JOB_BUTTON = (By.CSS_SELECTOR, "a[href*='/apply']")
    HOME_PAGE_LINK = (By.XPATH, "//a[contains(.,'Insider One Home Page')]")

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

        assert any("Quality Assurance" in job for job in jobs_list), f"Non of the jobs contain 'Quality Assurance'"

    def validate_all_jobs_contain_qa(self):
        jobs_elements = self.get_jobs()
        assert len(jobs_elements) > 0, "No jobs found"
        jobs_list = [job.text for job in jobs_elements]
        non_matching_jobs = [job for job in jobs_list if "Quality Assurance" not in job]

        assert not non_matching_jobs, f"Not all jobs contain 'Quality Assurance'. Non-matching jobs: {non_matching_jobs}"

    def validate_locations(self):
        location_elements = self.get_job_locations()
        assert len(location_elements) > 0, "No job locations found"
        location_list = [loc.get_attribute("text") for loc in location_elements]
        #Note: 'Istanbul, Turkiye' is in the list but not 'Istanbul,Turkey' leaving it regards to the requirement doc.
        assert "Istanbul, Turkiye" in location_list, "'Istanbul, Turkey' is not in the job locations"

    def validate_departments(self):
        department_elements = self.get_job_departments()
        assert len(department_elements) > 0, "No job departments found"
        department_list = [dept.get_attribute("text") for dept in department_elements]

        assert "Quality Assurance" in department_list, "'Quality Assurance' is not in the job departments"

    def click_apply(self):
        self.driver.find_element(*self.APPLY_BUTTON).click()

    def is_redirected_to_lever(self):
        try:
            self.wait.until(lambda d: "lever" in d.current_url)
        except TimeoutException:
            print("Lever URL not detected within wait window")

        apply_visible = self.element_exists(self.APPLY_FOR_JOB_BUTTON)
        home_visible = self.element_exists(self.HOME_PAGE_LINK)

        print(f"Lever checks -> urlHasLever: {'lever' in self.driver.current_url}, "
              f"applyVisible: {apply_visible},"
              f"homeVisible: {home_visible}")

        return ("lever" in self.driver.current_url and apply_visible and home_visible)

    def element_exists(self, locator):
        try:
            self.wait.until(lambda d: d.find_elements(*locator))
            return True
        except TimeoutException:
            return False