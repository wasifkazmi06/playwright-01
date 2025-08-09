from playwright.sync_api import Page
from pages.NewCarsPage import NewCarsPage


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.new_cars = page.locator("//div[normalize-space()='NEW CARS']")
        self.search_new_cars = page.get_by_role("link", name="Find New Cars")
        self.toyota_new_cars = page.get_by_role("link", name="Toyota Cars Toyota")
        self.bmw_new_cars = page.get_by_role("link", name="BMW Cars BMW")

    def find_new_cars(self):
        self.new_cars.click()
        self.search_new_cars.click()

        return NewCarsPage(self.page)

    def go_to_used_cars(self):
        pass

    def go_to_search_cars(self):
        pass
