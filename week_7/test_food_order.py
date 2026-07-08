from food_order import calculate_total

def test_order1():
    assert calculate_total(10, 2) == 20

def test_order2():
    assert calculate_total(10, 3) == 30

def test_order3():
    assert calculate_total(20, 5) == 100

def test_order4():
    assert calculate_total(5, 2) == 10

def test_order5():
    assert calculate_total(-1, 5) == "invalid price"

def test_order6():
    assert calculate_total(10, -2) == "invalid quantity"