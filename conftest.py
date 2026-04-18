from pathlib import Path
import pytest
from slugify import slugify
import allure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # We only care about the 'call' phase (when the test actually runs)
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")

        # FIX 1: Correct grouping and ensure 'page' exists
        if (report.failed or xfail) and "page" in item.funcargs:
            page = item.funcargs["page"]

            # Setup screenshot path
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")

            # Take the screenshot
            page.screenshot(path=screen_file)

            # FIX 2: Check if pytest-html is actually installed/active
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra.append(pytest_html.extras.png(screen_file))

            # Attach to Allure report (Check if file exists first)
            if Path(screen_file).exists():
                allure.attach.file(
                    screen_file,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

        report.extra = extra