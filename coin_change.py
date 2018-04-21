def change(cents):
    quarters = cents / 25
    remainder = cents - (quarters * 25)
    dimes = remainder / 10
    remainder = remainder - (dimes * 10)
    nickels = remainder / 5
    remainder = remainder - (nickels * 5)
    pennies = remainder

    my_dict = {
        'quarters': quarters,
        'dimes': dimes,
        'nickels': nickels,
        'pennies': pennies
    }
    print(my_dict)
change(90)