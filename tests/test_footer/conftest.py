import pytest
from pages.footer import Footer


@pytest.fixture()
def footer_open(driver, url):
    page = Footer(driver)
    driver.get(url)
    page.get_cookies_link().click()
    return page
