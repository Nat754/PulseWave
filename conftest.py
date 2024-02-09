import os
import shutil
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope='function')
def driver(browser):
    print(f'\nstart {browser} browser...')
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument('--headless')
        driver = webdriver.Edge(options=edge_options)
    yield driver
    print(f'\nquit {browser} browser...')
    driver.quit()


# скриншот
@allure.feature("Make a Screenshot")
def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        if call.excinfo is not None:
            try:
                driver = item.funcargs['driver']
                driver.save_screenshot('allure-results/screenshot.png')
                allure.attach.file('allure-results/screenshot.png', name='Screenshot',
                                   attachment_type=allure.attachment_type.PNG)
                allure.attach(driver.page_source, name="HTML source", attachment_type=allure.attachment_type.HTML)
            except Exception as e:
                print(f"Failed to take screenshot: {e}")


@pytest.fixture(scope="session", autouse=True)
def clear_allure_results_folder():
    allure_report_dir = "allure-results"
    if os.path.exists(allure_report_dir):
        for file_name in os.listdir(allure_report_dir):
            file_path = os.path.join(allure_report_dir, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
