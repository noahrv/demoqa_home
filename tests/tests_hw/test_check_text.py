from selenium.webdriver.common.by import By
from pages.base_page import BasePage

def test_footer_text(browser):
    page = BasePage(browser)
    page.visit()
    footer = browser.find_element(By.CSS_SELECTOR, 'footer span')
    assert footer.text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_center_text_on_elements_page(browser):
    page = BasePage(browser)
    page.visit()
    browser.find_element(By.CSS_SELECTOR, 'div.card').click()
    center_text = browser.find_element(By.CSS_SELECTOR, 'div.col-12.mt-4.col-md-6').text
    assert center_text == 'Please select an item from left to start practice.'