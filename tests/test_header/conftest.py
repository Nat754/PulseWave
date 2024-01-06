import pytest
from pages.header import HeaderPage


@pytest.fixture()
def header_open(driver, url):
    page = HeaderPage(driver)
    driver.get(url)
    page.get_allow_all_cookies().click()
    return page
