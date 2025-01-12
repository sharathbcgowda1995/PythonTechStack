from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Shop:
    #def __init__(self):


    @keyword
    def add_to_cart_and_checkout(self, productslist):
        print("Hi...")
        self.selLib = BuiltIn.get_library_instance("SeleniumLibrary")
        i = 1
        products = self.selLib.get_webelements("css:h4.card-title")
        for product in products:
            if product.text in productslist:
                self.selLib.click_button("xpath:(//*[@class='card-footer'])["+str(i)+"]/button")

            i=i=1
