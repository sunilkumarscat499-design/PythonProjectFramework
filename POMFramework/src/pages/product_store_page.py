from playwright.sync_api import Page
class ProductStorePage:

    def __init__(self,page:Page):
        self.page = page
        self.list_products = self.page.locator(".card-title>a")
        self.add_to_cart_button = self.page.locator("a[onclick='addToCart(1)']")
        self.cart_link = self.page.locator("#cartur")


    def click_on_product_add_cart(self,product_name):
        list_products = [self.page.locator(".card-title>a")]
        for product in list_products:
            if product.inner_text() == product_name:
                product.click()
                break

        self.page.on("dialog", lambda dialog:dialog.accept())
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.cart_link.click()
