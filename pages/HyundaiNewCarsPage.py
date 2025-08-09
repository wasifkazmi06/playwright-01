from playwright.sync_api import Page


class HyundaiNewCarsPage:

    def __init__(self, page: Page):
        self.hyundai_brand_heading = page.get_by_role("heading", name="Hyundai Cars").first

