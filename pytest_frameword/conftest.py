import pytest
import os
from datetime import datetime
import pytest_html

def pytest_html_report_title(report):
    report.title = "My HTML Report for Automation"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call':
        extras.append(pytest_html.extras.url("https://demo.automationtesting.in/Register.html"))

        if report.failed:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            screenshot_name = f"{item.name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)

            driver = item.funcargs.get('driver')
            if driver:
                driver.save_screenshot(screenshot_path)
                # Pass relative path to HTML report
                extras.append(pytest_html.extras.image(screenshot_path))
            else:
                print("❌ Driver not available to capture screenshot")

        report.extras = extras
