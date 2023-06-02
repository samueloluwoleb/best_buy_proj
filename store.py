class Store:

    def __init__(self, list_of_products_in_store_par):
        """
            creates and initializes the variable that holds the list of products in store.
        :param list_of_products_in_store_par:
        """
        self.list_of_products_in_store = list_of_products_in_store_par

    def add_product(self, product_par):
        """
            adds a new product to the list containing all store products
        :param product_par:
        :return:
        """
        self.list_of_products_in_store.append(product_par)

    def remove_product(self, product_par):
        """
            deletes a specified product from the list of products in store
        :param product_par:
        :return:
        """
        new_products_list = []
        for product in self.list_of_products_in_store:
            if product != product_par:
                new_products_list.append(product)
            else:
                continue
        self.list_of_products_in_store = new_products_list

    def get_total_quantity(self):
        """
            gets and return the total number of available products in store
        :return int:
        """
        total_product_quantity = 0
        for product in self.list_of_products_in_store:
            total_product_quantity += product.get_quantity()
        return int(total_product_quantity)

    def get_all_products(self):
        """
            Returns all products in the store that are active.
        :return list:
        """
        active_product_list = []
        for product in self.list_of_products_in_store:
            if product.is_active():
                active_product_list.append(product)
        return active_product_list

    @staticmethod
    def order(shopping_list_par):
        """
            Gets a list of tuples, where each tuple has 2 items: Product (Product class) and quantity (int).
            Buys the products and returns the total price of the order.
        :param shopping_list_par:
        :return float:
        """
        total_price = 0
        for product_obj, quantity in shopping_list_par:
            total_price += product_obj.buy(quantity)
        return total_price
