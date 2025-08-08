
class NewCarsPage():

    def __init__(self, page):
        self.page = page
        self.toyota_new_cars = page.get_by_role("link", name="Toyota Cars Toyota")
        self.bmw_new_cars = page.get_by_role("link", name="BMW Cars BMW")
        self.read_more_link = page.get_by_label("Read More")

    def go_to_toyota(self):
        self.toyota_new_cars.click()

    def go_to_bmw(self):
        self.bmw_new_cars.click()

    def go_to_honda(self):
        pass

    def go_to_mg(self):
        pass
