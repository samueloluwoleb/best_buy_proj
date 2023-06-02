# setup initial stock of inventory
import products
import store
import promotions

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


def display_menu():
    """
        displays the user interface menu for the user to interact with
    :return:
    """
    print(f'     Store Menu \n     ----------\n1. List all products in store\n'
          f'2. Show total amount in store \n3. Make an order \n4. Quit \nPlease choose a number: ', end='')


def list_all_products():
    """
        lists and displays all products in store that have quantity greater than zero
    :return:
    """
    temp_list_holder = []
    print('------')
    for product in best_buy.list_of_products_in_store:
        if product.is_active():
            temp_list_holder.append(product)
    best_buy.list_of_products_in_store = temp_list_holder
    for count, product in enumerate(best_buy.list_of_products_in_store):
        print(f'{count + 1} {product.show()}')
    print('------')


def show_total_amount():
    """
        shows the total number of available products in store
    :return:
    """
    total_amount_products = best_buy.get_total_quantity()
    print(f'\nTotal of {total_amount_products} items in store\n')


def make_order():
    """
        gets menu number and product quantity user wants to purchase from user and
        updates the store accordingly
    :return:
    """
    list_all_products()
    print(f'\nWhen you want to finish order, enter empty text.', end='')
    while True:
        print('\nWhich product # do you want? ', end='')
        user_input_product = input()
        user_input_quantity = input('What amount do you want? ')
        if user_input_product == '' and user_input_quantity == '':
            break
        if len(best_buy.list_of_products_in_store) == 0:
            print('\nSorry, you can\'t make an order, there are no products in store\n')
            break
        elif user_input_quantity.isnumeric() and user_input_product.isnumeric():
            if int(user_input_product) in range(len(best_buy.list_of_products_in_store) + 1):
                for count, product in enumerate(best_buy.list_of_products_in_store):
                    if count + 1 == int(user_input_product) and type(product) is products.LimitedProduct:
                        if int(user_input_quantity) > 1:
                            print('You can\'t order more than 1 of this product')
                        if int(user_input_quantity) == 1:
                            store.Store.order([(product, int(user_input_quantity))])
                    if count + 1 == int(user_input_product) and type(product) is not products.LimitedProduct:
                        original_quantity = product.get_quantity()
                        store.Store.order([(product, int(user_input_quantity))])
                        if product.get_quantity() == original_quantity and type(product) is products.Product:
                            print(f'You requested for more than the available quantity in store, '
                                  f'quantity should not be more than {int(product.get_quantity())}')
                        else:
                            print('Product added to list!')
            else:
                print('Enter the right number corresponding to the product in store')
        else:
            print('Check your product and quantity input and try again')


def start():
    while True:
        display_menu()
        user_input = input()
        if user_input == '1':
            list_all_products()
        elif user_input == '2':
            show_total_amount()
        elif user_input == '3':
            make_order()
        elif user_input == '4':
            quit()
        else:
            continue


def main():
    """
        runs the start function that
    :return:
    """
    start()


if __name__ == '__main__':
    main()
