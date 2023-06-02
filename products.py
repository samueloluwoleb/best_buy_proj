import promotions


class Product:

    def __init__(self, name, price, quantity):
        """
            Initiator (constructor) method.
            Creates the instance variables (active is set to True).
        :param name:
        :param price:
        :param quantity:
        """
        self.Promotion = ''
        self.Active = True
        self.Name = name
        if type(price) is int and price > 0:
            self.Price = price
        else:
            self.Price = 0
        if type(quantity) is int and quantity > 0:
            self.Quantity = quantity
        else:
            self.product_quantity = 0
            self.deactivate()

    def get_quantity(self):
        """
            Getter function for quantity.
            Returns the quantity.
        :return float:
        """
        return float(self.Quantity)

    def set_quantity(self, quantity):
        """
            Setter function for quantity. If quantity reaches 0, deactivates the product.
        :param quantity:
        :return:
        """
        self.Quantity -= int(quantity)
        if self.Quantity == 0:
            self.deactivate()

    def is_active(self):
        """
            Getter function for active.
            Returns True if the product is active, otherwise False.
        :return bool:
        """
        if self.Active:
            return True
        else:
            return False

    def activate(self):
        """
            Activates a product
        :return:
        """
        self.Active = True

    def deactivate(self):
        """
            deactivates a product
        :return:
        """
        self.Active = False

    def show(self):
        """
            Returns a string that represents the product
        :return:
        """
        if self.Promotion == '':
            return f"{self.Name}, Price: {self.Price}, Quantity: {self.Quantity}, Promotion: None"
        else:
            return f"{self.Name}, Price: {self.Price}, Quantity: {self.Quantity}, Promotion: {self.Promotion.Name}"

    def buy(self, quantity):
        """
            Buys a given quantity of the product.
            Returns the total price of the purchase.
            Updates the quantity of the product.
        :param quantity:
        :return float:
        """
        self.set_quantity(quantity)
        if self.Promotion == '':
            if self.get_quantity() < 0:
                self.set_quantity(-quantity)
            if self.get_quantity() > 0:
                price_of_purchase = self.Price * quantity
                return price_of_purchase
        elif type(self.Promotion) is promotions.SecondHalfPrice and int(quantity) == 1:
            if self.get_quantity() < 0:
                self.set_quantity(-quantity)
            if self.get_quantity() > 0:
                price_of_purchase = self.Price * quantity
                return price_of_purchase
        elif type(self.Promotion) is promotions.ThirdOneFree and int(quantity) < 3:
            if self.get_quantity() < 0:
                self.set_quantity(-quantity)
            if self.get_quantity() > 0:
                price_of_purchase = self.Price * quantity
                print(price_of_purchase)
                return price_of_purchase
        elif self.Promotion != '':
            price_of_purchase = self.Promotion.apply_promotion(self, quantity)
            if self.get_quantity() < 0:
                self.set_quantity(-quantity)
            if self.get_quantity() > 0:
                print(price_of_purchase)
                return price_of_purchase

    def set_promotion(self, promo_obj):
        self.Promotion = promo_obj

    def get_promotion(self):
        return self.Promotion


class NonStockedProduct(Product):

    def __init__(self, name, price):
        self.Active = True
        self.Name = name
        if type(price) is int and price > 0:
            self.Price = price
        else:
            self.Price = 0
        self.Quantity = False

    def get_quantity(self):
        """
            Does nothing and returns None
        :return None:
        """
        return 0

    def set_quantity(self, quantity):
        """
            Does nothing since there is no quantity attribute for this object
        :return None:
        """
        pass

    def buy(self, quantity):
        """
            Buys a given quantity of the product.
        :param quantity:
        :return float:
        """
        # testing price of purchase
        if self.Promotion == '':
            price_of_purchase = self.Price
            return price_of_purchase
        else:
            price_of_purchase = self.Promotion.apply_promotion(self, quantity)
            return price_of_purchase

    def show(self):
        """
            Returns a string that represents the product
        :return:
        """
        return f"{self.Name}, Price: {self.Price}, Quantity: Unlimited, Promotion: {self.Promotion.Name}"


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum
