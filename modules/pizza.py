def make_pizza(size, *toppings):
    print('You have ordered the pizza with following:')
    
    for topping in toppings:
        print(f"- {topping}")

    return f"size: {size}"

