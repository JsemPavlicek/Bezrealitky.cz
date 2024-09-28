# # test case - Abstract: Using Python Playwright to verify, if an element anchor with text
#  Potřebuji advokátní služby is visible for Samsung Galaxy S8 device on the website bezrealitky.cz

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # for one_device_key in p.devices.keys():
    #     print(one_device_key)
    samsung_galaxy_S8 = p.devices['Galaxy S8']
    browser = p.chromium.launch(channel="chromium", headless= False)
    page = browser.new_page(**samsung_galaxy_S8)
    page.goto('https://bezrealitky.cz')
    cookies = page.locator('button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    cookies.click()
    page.wait_for_load_state('networkidle')
    screen_width = samsung_galaxy_S8['viewport']['width']
    screen_height = samsung_galaxy_S8['viewport']['height']
    device_screen = [screen_width, screen_height]
    #print(device_screen)

    page.mouse.wheel(0, 1000)
    a_href_legal_services = page.locator('a:has-text("Potřebuji advokátní služby")')
    if a_href_legal_services.is_visible():
        print(f"element s textem {a_href_legal_services.inner_text()} is visible in the viewport of Samsung Galaxy S8")
        page.screenshot(path='a_href_legal_services_visibility.png')
    page.wait_for_timeout(10000)
    browser.close()





