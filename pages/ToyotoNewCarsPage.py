from playwright.sync_api import Page


class ToyotaNewCarsPage:

    def __init__(self, page: Page):
        self.toyota_brand_heading = page.get_by_role("heading", name="Toyota Cars").first

