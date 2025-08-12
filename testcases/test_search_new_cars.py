import allure
import pytest
from playwright.sync_api import expect
from pages.HomePage import HomePage
from testcases.BaseTest import BaseTest
from utilities import dataProvider


class TestSearchNewCars(BaseTest):

    @allure.feature("Find New Cars Test")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("page, browser", [(("url", "car_wale_url"), "chrome"),
                                               (("url", "car_wale_url"), "firefox")], indirect=True)
    def test_finding_new_cars(self, page):
        with allure.step("*****Executing Finding New Cars Test*****"):
            home = HomePage(page)
            home.find_new_cars()
            expect(home.find_new_cars().toyota_new_cars).to_be_visible()
            expect(home.find_new_cars().read_more_link).to_be_enabled()

    @allure.feature("Find New Cars Test")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("page, browser", [(("url", "car_wale_url"), "chrome"),
                                               (("url", "car_wale_url"), "firefox")], indirect=True)
    def test_finding_new_toyota_cars(self, page):
        with allure.step("*****Executing Finding New Toyota Cars Test*****"):
            home = HomePage(page)
            home.find_new_cars().go_to_toyota()
            expect(home.find_new_cars().go_to_toyota().toyota_brand_heading).to_be_visible()

    @allure.feature("Find New Cars Test")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("car_brand, car_title", dataProvider.read_csv_data("car_data_csv_path"))
    @pytest.mark.parametrize("page, browser", [(("url", "car_wale_url"), "chrome"),
                                               (("url", "car_wale_url"), "firefox")], indirect=True)
    def test_finding_new_cars_other_brands(self, page, car_brand, car_title):
        with allure.step("*****Executing Finding New Cars Other Brands Test*****"):
            home = HomePage(page)
            home.find_new_cars()
            print(car_brand, car_title)
            if car_brand == "BMW":
                home.find_new_cars().go_to_bmw()
                expect(home.find_new_cars().go_to_bmw().bmw_brand_heading).to_have_text(car_title)
            elif car_brand == "Hyundai":
                home.find_new_cars().go_to_hyundai()
                expect(home.find_new_cars().go_to_hyundai().hyundai_brand_heading).to_have_text(car_title)
            elif car_brand == "MG":
                home.find_new_cars().go_to_mg()
                expect(home.find_new_cars().go_to_mg().mg_brand_heading).to_have_text(car_title)
            else:
                print("Incorrect car brand!")
