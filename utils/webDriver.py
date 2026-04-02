from selenium import webdriver

def get_driver(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception("Unsupported browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver