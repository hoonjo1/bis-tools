from selenium import webdriver

def selenuim_start_f():
    driver = r"\\kjnas\KJNAS\1.기획부\9.개발팀\chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
    "download.default_directory": r"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_SCORE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,})
    driver = webdriver.Chrome(driver, chrome_options=options)
    return driver

def selenuim_start_f_bus_info():
    driver = r"\\kjnas\KJNAS\1.기획부\9.개발팀\chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
    "download.default_directory": r"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\BEFORE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,})
    driver = webdriver.Chrome(driver, chrome_options=options)
    return driver

