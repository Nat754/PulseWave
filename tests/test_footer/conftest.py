import pytest
from pages.footer import FooterPage


@pytest.fixture()
def footer_open(driver, url):
    page = FooterPage(driver)
    driver.get(url)
    page.get_cookies_link()
    return page
