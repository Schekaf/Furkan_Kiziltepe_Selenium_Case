import pytest
from utils.webDriver import get_driver
from utils.screenshot import take_screenshot

from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAPage

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_insider(browser):

    driver = get_driver(browser)

    try:
        # 1. Home page
        home = HomePage(driver)
        home.open("https://insiderone.com/")
        assert home.is_loaded()
        assert home.has_main_blocks()

        # 2. Careers page
        careers = CareersPage(driver)
        careers.open("https://insiderone.com/careers/#open-roles")
        careers.click_see_all_teams()
        careers.open_qa_positions()

        # 3. QA jobs validation
        qa = QAPage(driver)
        #qa.validate_jobs()
        #qa.validate_departments()
        #qa.validate_locations()

        # 4. Apply button check
        qa.click_apply()
        assert qa.is_redirected_to_lever()

    except Exception as e:
        take_screenshot(driver, "failure")
        raise e

    finally:
        driver.quit()