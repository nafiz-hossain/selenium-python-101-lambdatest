import pytest

def test_drag_drop_slider(driver):
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.find_element_by_link_text("Drag & Drop Sliders").click()
    assert "drag-drop-range-sliders" in driver.current_url

    slider = driver.find_element_by_xpath("//input[@type='range' and @value='15']")
    driver.execute_script("arguments[0].value = arguments[1]", slider, 95)

    range_value = driver.find_element_by_id("rangeSuccess").text
    assert range_value == "95"