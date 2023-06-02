from abc import ABC, abstractmethod


class Promotion(ABC):
    """
        An abstract class with an abstract method apply promotion to define promotion classes
    """
    name = ''

    def add_promotion(self, product_obj):
        """
            Adds a promotion to a product object
        :param product_obj:
        :return:
        """
        product_obj.set_promotion(self)
        print('Promotion successfully added')

    @staticmethod
    def remove_promotion(product_obj):
        """
            removes promotion from an abstract object
        :param product_obj:
        :return:
        """
        if product_obj.get_promotion() is not None:
            product_obj.Promotion = ''
        else:
            print('The items has not promotion')

    @abstractmethod
    def apply_promotion(self, product_obj, quantity):
        """
            An abstract method that all subclasses are inherited from
        :param product_obj:
        :param quantity:
        :return:
        """
        pass


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        """
            A constructor to initialize the Name parameter
        :param name:
        """
        self.Name = name

    def apply_promotion(self, product, quantity):
        """
            Gets 2 parameters - a product instance and a quantity, and returns
            the discounted price after promotion was applied.
        :param product:
        :param quantity:
        :return:
        """
        price_of_2 = product.Price * 1.5
        if quantity == 2:
            return price_of_2
        elif quantity > 2:
            if quantity % 2 == 0:
                temp_quantity = quantity / 2
                total_price = price_of_2 * temp_quantity
                return total_price
            if quantity % 2 != 0:
                temp_quantity = quantity // 2
                total_price = (price_of_2 * temp_quantity) + product.Price
                return total_price


class ThirdOneFree(Promotion):

    def __init__(self, name):
        """
            A constructor to initialize the Name parameter
        :param name:
        """
        self.Name = name

    def apply_promotion(self, product, quantity):
        """
            Gets 2 parameters - a product instance and a quantity, and returns
            the discounted price after promotion was applied.
        :param product:
        :param quantity:
        :return:
        """
        price_of_3 = product.Price * 2
        if quantity == 3:
            return price_of_3
        elif quantity > 3:
            if quantity % 3 == 0:
                temp_quantity = quantity / 3
                total_price = price_of_3 * temp_quantity
                return total_price
            if quantity % 3 == 1:
                temp_quantity = quantity // 3
                total_price = (price_of_3 * temp_quantity) + product.Price
                return total_price
            if quantity % 3 == 2:
                temp_quantity = quantity // 3
                total_price = (price_of_3 * temp_quantity) + (product.Price * 2)
                return total_price


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        """
            A constructor to initialize the Name parameter
        :param name:
        :param percent:
        """
        self.Name = name
        self.Percent = percent

    def apply_promotion(self, product, quantity):
        """
            Gets 2 parameters - a product instance and a quantity, and returns
            the discounted price after promotion was applied.
        :param product:
        :param quantity:
        :return:
        """
        original_price = product.Price
        percent = self.Percent
        new_price = original_price - (percent * original_price) / 100
        return new_price
