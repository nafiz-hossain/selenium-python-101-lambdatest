# Selenium Python 101 LambdaTest Certification

## Overview

This repository contains automated test scripts developed for the LambdaTest Selenium 101 Certification. The tests cover essential scenarios using Selenium WebDriver in Python, executed on LambdaTest's Selenium Grid across multiple browser and operating system combinations.

## Test Scenarios

### Test Scenario 1: Simple Form Demo
1. Open LambdaTest’s Selenium Playground.
2. Click "Simple Form Demo" under Input Forms.
3. Validate URL contains "simple-form-demo".
4. Enter message into "Enter Message" textbox.
5. Click "Get Checked Value" and validate displayed message.

### Test Scenario 2: Drag & Drop Sliders
1. Open Selenium Playground and click "Drag & Drop Sliders".
2. Drag slider "Default value 15" to make it 95.
3. Validate the range value displays 95.

### Test Scenario 3: Input Form Submit
1. Open Selenium Playground and click "Input Form Submit".
2. Click "Submit" without filling any form fields.
3. Assert "Please fill in the fields" error message.
4. Fill in Name, Email, and other fields.
5. Select "United States" from the Country dropdown.
6. Fill all fields and click "Submit".
7. Validate success message "Thanks for contacting us, we will get back to you shortly."

## Execution

These scenarios are demonstrated on the following browser and operating system combinations using Selenium 4 Grid:

1. Chrome 88.0 on Windows 10
2. MicrosoftEdge 87.0 on macOS Sierra
3. Firefox 82.0 on Windows 7
4. Internet Explorer 11.0 on Windows 10

## Important Notes

- Use your preferred version of the Python framework, preferably the latest.
- Utilize a data-driven approach to pass browser and OS combinations.
- Setup and teardown functions should not be part of the @Test annotation.
- Set a timeout of 20 seconds for test duration and ensure parallel execution.
- Use at least 3 different locators during test implementation.
- Enable network logs, video recording, screenshots, and console logs via Capability Generator.
- Follow detailed submission guidelines for final test execution and reporting.

---
