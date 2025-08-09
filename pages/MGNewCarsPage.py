from playwright.sync_api import Page


class MGNewCarsPage:

    def __init__(self, page: Page):
        self.mg_brand_heading = page.get_by_role("heading", name="MG Cars").first

