import pytest

def test_simple_form_demo(driver):
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.find_element_by_link_text("Simple Form Demo").click()
    assert "simple-form-demo" in driver.current_url

    message = "Welcome to LambdaTest"
    driver.find_element_by_id("user-message").send_keys(message)
    driver.find_element_by_id("showInput").click()

    displayed_message = driver.find_element_by_id("message").text
    assert displayed_message == message