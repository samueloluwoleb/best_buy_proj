from best_buy_proj.products import Product

product_obj1 = Product("MacBook Air M2", price=1450, quantity=100)
product_obj1.set_quantity(50)

product_obj2 = Product("Bose QuietComfort Earbuds", price=-50, quantity=100)

product_obj3 = Product("Google Pixel 7", price=150, quantity=0)

product_obj4 = Product("Bose Mouse", price=500, quantity=100)
product_obj4.buy(200)


def test_creating_prod():
    assert product_obj1.Name == "MacBook Air M2"


def test_creating_prod_invalid_details():
    assert product_obj2.Price == 0


def test_prod_becomes_inactive():
    assert product_obj3.is_active() is False


def test_buy_modifies_quantity():
    assert product_obj1.get_quantity() == 50


def test_buy_too_much():
    assert product_obj4.get_quantity() == 100
