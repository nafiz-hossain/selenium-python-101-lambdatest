import pytest

def test_input_form_submit(driver):
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.find_element_by_link_text("Input Form Submit").click()
    assert "input-form-demo" in driver.current_url

    driver.find_element_by_xpath("//button[text()='Submit']").click()
    error_message = driver.find_element_by_xpath("//p[text()='Please fill in the fields']").text
    assert error_message == "Please fill in the fields"

    driver.find_element_by_name("name").send_keys("Test Name")
    driver.find_element_by_name("email").send_keys("test@example.com")
    driver.find_element_by_name("country").send_keys("United States")
    driver.find_element_by_xpath("//button[text()='Submit']").click()

    success_message = driver.find_element_by_xpath("//div[text()='Thanks for contacting us, we will get back to you shortly.']").text
    assert success_message == "Thanks for contacting us, we will get back to you shortly."