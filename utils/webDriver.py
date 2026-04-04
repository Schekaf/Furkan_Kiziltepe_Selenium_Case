from selenium import webdriver

CHROME_ARGUMENTS = [
    "--disable-notifications", "--no-sandbox", "--disable-dev-shm-usage"
]

FIREFOX_OPTIONS = [
    "--disable-notifications"
]


def get_driver(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=get_options(CHROME_ARGUMENTS, options))
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=get_options(FIREFOX_OPTIONS, options))
    else:
        raise Exception("Unsupported browser")

    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver


def get_options(args, options):
    for arg in args:
        options.add_argument(arg)
    return options
