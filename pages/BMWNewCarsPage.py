from playwright.sync_api import Page


class BMWNewCarsPage:

    def __init__(self, page: Page):
        self.bmw_brand_heading = page.get_by_role("heading", name="BMW Cars").first

