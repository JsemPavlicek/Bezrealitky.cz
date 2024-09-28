# test case - Abstract: Using Python Playwright for test verify on the website bezrealitky.cz, if an offer of property
# are sorted in ascending order after click on the select option "Nejlevnější"

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(channel='chrome', headless=False, slow_mo= 500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bezrealitky.cz")

    cookies = page.locator('button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    if cookies.count() > 0:
        cookies.click()
    type_of_property = page.locator('button:has-text("Nemovitost")')
    type_of_property.click()
    radio_button_house = page.locator('#DUM')
    radio_button_house.check()
    search_button = page.locator('button[class="d-none d-md-block SearchPanel_searchPanelButton__FSMKl btn-lg btn btn-primary"]')
    search_button.click()
    page.wait_for_timeout(10000)
    dropdown_sell_or_rent = page.locator('path[d="M12 15L7 9h10z"]').nth(0)
    dropdown_sell_or_rent.click()
    sell = page.locator('text="Prodej"').nth(1)
    sell.click()
    select_property = page.locator('div.dropdown-heading-value')
    # print(select_property.count())
    select_property.nth(1).click()
    house = page.locator('text="Dům"').nth(0)
    house.click()
    concrete_search_button = page.locator('button >> span:has-text("Vyhledat")')
    concrete_search_button.click()
    sort_select_option = page.select_option('#order-by', value="PRICE_ASC")
    page.wait_for_timeout(10000)
    sorted_prices_ASC = page.locator('span.PropertyPrice_propertyPriceAmount__WdEE1')

    # Finding out, how many advertisiments are visible at the moment
    number_of_sorted_prices_ASC = sorted_prices_ASC.count()
    # print(number_of_sorted_prices_ASC)


    # Storing prices from elements into the list prices_array_string
    prices_string = ""
    prices_array_string = []
    for i in range(number_of_sorted_prices_ASC):
        prices_string = ""
        one_price_string = sorted_prices_ASC.nth(i).inner_text()
        for one_char in one_price_string:
            if one_char.isnumeric():
                prices_string += one_char
        prices_array_string.append(prices_string)

    # convert list of strings to numbers
    for i in range(len(prices_array_string)):
        prices_array_string[i] = int(prices_array_string[i])

    # print(prices_array_string)
    print(f"{len(prices_array_string)} prices were found")
    for i in range(len(prices_array_string) - 1):
        assert prices_array_string[i] < prices_array_string[i + 1]
    context.close()
    browser.close()
print("No bugs were found, prices are sorted by ascending order correctly")













