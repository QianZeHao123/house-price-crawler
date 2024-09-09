import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://zz.lianjia.com/")
    page.get_by_placeholder("请输入区域、商圈或小区名开始找房").click()
    page.get_by_placeholder("请输入区域、商圈或小区名开始找房").fill("金水区")
    page.get_by_role("button", name="开始找房").click()

    


with sync_playwright() as playwright:
    run(playwright)