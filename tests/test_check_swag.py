from pages.swag_labs import SwagLabs


class TestSwagLabs:
    def test_check_icon_existence(self, browser):
        swag_page = SwagLabs(browser)
        swag_page.visit()
        assert swag_page.exist_icon()

    def test_check_username_field_existence(self, browser):
        swag_page = SwagLabs(browser)
        swag_page.visit()
        assert swag_page.find_element('input#user-name')

    def test_check_password_field_existence(self, browser):
        swag_page = SwagLabs(browser)
        swag_page.visit()
        assert swag_page.find_element('input#password')