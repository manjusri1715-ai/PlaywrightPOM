class resultsPage:
    def __init__(self, page):
        self.addTcart =lambda product: page.locator(f"(//h2[contains(@aria-label,'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//*[@aria-label='Add to cart'])[1]")
        self.addTcart_iphoneAir = page.locator("(//h2[contains(@aria-label,'iPhone Air')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//*[@aria-label='Add to cart'])[1]")

    def clickOnAddToCart(self,product):
        self.addTcart(product).click()


    # def sum(a,b):
    #     print(a+b)

    # sum = lambda a,b:print(a+b)

    