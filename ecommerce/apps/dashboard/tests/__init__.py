import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, chrome_browser_instance):
    """
    Test the admin login functionality of the Django dashboard.
    This test uses Selenium to automate browser actions. It navigates to the Django admin login page,
    enters valid credentials, and checks if the login is successful by verifying the title of the
    resulting page.
    Args:
        live_server (LiveServerTestCase): A pytest-django fixture, which is an instance of the running Django server.
        chrome_browser_instance (WebDriver): A Selenium WebDriver instance for the Chrome browser.
    """
    browser = chrome_browser_instance
    browser.get((f"{live_server.url}/admin/login/"))

    assert "Log in | Django site admin" in browser.title

    username = browser.find_element(By.CSS_SELECTOR, "input#id_username")
    username.send_keys("admin")

    password = browser.find_element(By.CSS_SELECTOR, "input#id_password")
    password.send_keys("admin")

    submit = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit.send_keys(Keys.RETURN)

    assert "Site administration | Django site admin" in browser.title