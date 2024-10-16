import pytest
from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from HW9.utils import attach


@pytest.fixture(scope="function")
def setup_browser(request):
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com/automation-practice-form/"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.page_load_strategy = "eager"
    # options.add_argument('--headless')
    browser.config.driver_options = options
    browser.config.driver.maximize_window()

    yield
    browser.quit()
