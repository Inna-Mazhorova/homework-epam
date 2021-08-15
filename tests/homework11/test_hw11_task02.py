from homework11.hw11_task02 import Order, elder_discount, morning_discount


def test_morning_discount():
    order1 = Order(100, discount_strategy=morning_discount)
    assert order1.final_price() == 75


def test_elder_discount():
    order2 = Order(100, discount_strategy=elder_discount)
    assert order2.final_price() == 90


def test_no_discount_case():
    order3 = Order(100)
    assert order3.final_price() == 100
