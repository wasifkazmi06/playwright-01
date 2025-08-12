from pages.BMWNewCarsPage import BMWNewCarsPage
from pages.HyundaiNewCarsPage import HyundaiNewCarsPage
from pages.MGNewCarsPage import MGNewCarsPage
from pages.ToyotoNewCarsPage import ToyotaNewCarsPage


class NewCarsPage:

    def __init__(self, page):
        self.page = page
        self.toyota_new_cars = page.get_by_role("link", name="Toyota Cars Toyota")
        self.bmw_new_cars = page.get_by_role("link", name="BMW Cars BMW")
        self.hyundai_new_cars = page.get_by_role("link", name="Hyundai Cars Hyundai")
        self.mg_new_cars = page.get_by_role("link", name="MG Cars MG")
        self.read_more_link = page.get_by_label("Read More")

    def go_to_toyota(self):
        self.toyota_new_cars.click()
        return ToyotaNewCarsPage(self.page)

    def go_to_bmw(self):
        self.bmw_new_cars.click()
        return BMWNewCarsPage(self.page)

    def go_to_hyundai(self):
        self.hyundai_new_cars.click()
        return HyundaiNewCarsPage(self.page)

    def go_to_mg(self):
        self.mg_new_cars.click()
        return MGNewCarsPage(self.page)
