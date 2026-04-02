from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    def is_loaded(self):
        return self.driver.find_element(By.TAG_NAME, "body").is_displayed()

    def has_main_blocks(self):
        # Adjust selectors if needed
        blocks = self.driver.find_elements(By.CSS_SELECTOR, "section")
        return len(blocks) > 0