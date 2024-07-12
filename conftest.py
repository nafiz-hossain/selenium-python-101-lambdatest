import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(params=[
    {'browser': 'Chrome', 'version': '88.0', 'platform': 'Windows 10'},
    {'browser': 'MicrosoftEdge', 'version': '87.0', 'platform': 'macOS Sierra'},
    {'browser': 'Firefox', 'version': '82.0', 'platform': 'Windows 7'},
    {'browser': 'Internet Explorer', 'version': '11.0', 'platform': 'Windows 10'}
])
def driver(request):
    browser = request.param['browser']
    version = request.param['version']
    platform = request.param['platform']
    
    lt_options = {
        "username": "nhremon8181",
        "accessKey": "gLe7TVx7ANAWuoi6iDeFPj7MNcMOSSlFam4b6VYDEmiMkeZWgk",
        "visual": True,
        "video": True,
        "resolution": "1366x768",
        "network": True,
        "build": "Selenium Python 101 Build",
        "project": "Selenium Python 101",
        "buildTags": ["Selenium", "Python"],
        "name": f"Test Scenario - {browser} {version} {platform}",
        "selenium_version": "4.0.0",
        "w3c": True,
        "plugin": "python-python"
    }

    options = ChromeOptions()
    options.browser_version = version
    options.platform_name = platform
    options.set_capability('LT:Options', lt_options)

    driver = webdriver.Remote(
        command_executor='https://nhremon8181:gLe7TVx7ANAWuoi6iDeFPj7MNcMOSSlFam4b6VYDEmiMkeZWgk@hub.lambdatest.com/wd/hub',
        options=options
    )
    yield driver
    driver.quit()