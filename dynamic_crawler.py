from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://equippo.bamboohr.com/jobs/view.php?id=97&source=bamboohr
    page.goto(
        "https://equippo.bamboohr.com/jobs/view.php?id=97&source=bamboohr"
    )

    # Click text=Apply for This Job Link to this job >> button
    page.locator("text=Apply for This Job Link to this job >> button").click()

    breakpoint()
    # Click button:has-text("Submit Application")
    page.locator('button:has-text("Submit Application")').click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
