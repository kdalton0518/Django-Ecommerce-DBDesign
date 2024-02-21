import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a Chrome browser instance for Selenium tests.
    This fixture creates a Chrome WebDriver instance with specific options suitable for testing.
    The browser runs in headless mode (without a GUI), with GPU disabled, and with a window size of 1920x1080.
    The instance is yielded for use in the tests, and quit after all tests in the session have run.
    Args:
        request (pytest.FixtureRequest): The pytest request object. This is a special object injected by the pytest framework,
                                         which provides information about the current test run.
    Yields:
        WebDriver: A Selenium WebDriver instance for the Chrome browser.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    yield browser

    browser.close()
