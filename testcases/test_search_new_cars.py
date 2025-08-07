import allure
from playwright.sync_api import expect
from pages.HomePage import HomePage
from pages.NewCarsPage import NewCarsPage
from testcases.BaseTest import BaseTest


class TestSearchNewCars(BaseTest):

    @allure.feature("Find New Cars Test")
    @allure.severity(allure.severity_level.MINOR)
    def test_finding_new_toyota_cars(self, page):
        with allure.step("*****Executing Finding New Toyota Cars Test*****"):
            home = HomePage(page)
            home.find_new_cars()
            new_car = NewCarsPage(page)
            expect(new_car.toyota_new_cars).to_be_visible()
            #home.go_to_toyota(page)
