public_toilet = "PB"


def home():
    private_toilet = "PT"
    print(public_toilet)
    print(private_toilet)


def stranger():
    print(public_toilet)
    # print(private_toilet)


print(public_toilet)

# If we are using outside then global variable will be picked up but if we are using
# inside then local will be prefer, Local V are always prefered over global
