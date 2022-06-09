#!/usr/bin/env python


"""
Apply for the job

"""
import time

import users
from playwright.sync_api import Playwright, sync_playwright
from playwright_stealth import stealth_sync


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    stealth_sync(page)
    # Go to https://thehub.io/jobs/625fcb2a7f91b0a1ffb2c98f
    page.goto("https://thehub.io/jobs/625fcb2a7f91b0a1ffb2c98f")

    # wait for the page to load
    page.click("text=OK")
    # Click text=Apply
    page.click("text=Apply")
    # Click text=OK
    # Click [placeholder="Email"]
    page.click('[placeholder="Email"]')

    # Fill [placeholder="Email"]
    page.fill('[placeholder="Email"]', users.user["email"])

    # Click [placeholder="Your name"]
    page.click('[placeholder="Your name"]')

    # Fill [placeholder="Your name"]
    page.fill('[placeholder="Your name"]', users.user["name"])

    # Click [placeholder="Phone number"]
    page.click('[placeholder="Phone number"]')

    # Fill [placeholder="Phone number"]
    page.fill('[placeholder="Phone number"]', users.user["phone"])

    # Click [placeholder="Current or previous job title"]
    page.click('[placeholder="Current or previous job title"]')

    # Fill [placeholder="Current or previous job title"]
    page.fill(
        '[placeholder="Current or previous job title"]', users.user["title"]
    )

    # Click [placeholder="Link to your LinkedIn profile"]
    page.click('[placeholder="Link to your LinkedIn profile"]')

    # Fill [placeholder="Link to your LinkedIn profile"]
    page.fill(
        '[placeholder="Link to your LinkedIn profile"]', users.user["linkedin"]
    )

    # Click [placeholder="Link to your Github"]
    page.click('[placeholder="Link to your Github"]')

    # Fill [placeholder="Link to your Github"]
    page.fill('[placeholder="Link to your Github"]', users.user["github"])

    # Click button:has-text("Select file")
    with page.expect_file_chooser() as fc_info:
        page.click('button:has-text("Select file")')
    file_chooser = fc_info.value
    file_chooser.set_files(users.user["profile_path"])

    name = page.locator("//iframe[@title='reCAPTCHA']").get_attribute("name")
    recaptcha = page.frame(name=name)
    page.click('div[role="document"] button:has-text("Apply")')
    token = page.query_selector('//input[@id="recaptcha-token"]')
    while token is None:
        print("Waiting for recaptcha")
        time.sleep(4)
        recaptch_check = page.query_selector(
            '//div[@class="recaptcha-checkbox-checkmark"]'
        )
        if recaptch_check is not None:
            print("Recaptcha Checked")
        page.query_selector('//input[@id="recaptcha-token"]')
        name = page.locator("//iframe[@title='reCAPTCHA']").get_attribute(
            "name"
        )
        if name:
            stealth_sync(page)
            page.frame(name=name).click('span[role="checkbox"]')
            time.sleep(2)
            page.click('div[role="document"] button:has-text("Apply")')
            time.sleep(4)
            # breakpoint()
            check_status = page.query_selector(
                '//h5[contains(text(),"Your job is saved in your dashboard")]'
            )
            if check_status:
                print("Job Applied")
                return {"status": "success"}
            else:
                frame_check = page.frame(name=name)
                if frame_check:
                    page.frame(name=name).click('span[role="checkbox"]')
                    time.sleep(2)
                    page.click('div[role="document"] button:has-text("Apply")')
                    print("Job not Applied")
                else:
                    print("Job Applied")
                    return {"status": "success"}
        token = page.query_selector('//input[@id="recaptcha-token"]')
        if token:
            token = token.get_property("value")

    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
