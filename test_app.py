from app import change, multiply


def test_change():
    assert [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] == change(1.34)


def test_multiply():
    assert [{500: "quarters"}, {100: "nickels"}, {400: "pennies"}] == multiply(1.34)
