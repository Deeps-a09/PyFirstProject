# Can we pass unlimited type of arguments- No

def make_pizza(*toppings, base):
    print(toppings, base)


make_pizza("mushroom", "onion", base="Thin Crust")


# * position should be first
def make_pizza(base, *toppings):
    print(base, toppings)


make_pizza("mushroom", "onion", base="Thin Crust")
