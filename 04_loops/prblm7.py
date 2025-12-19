"""
Docstring for 04_loops.prblm7
Some chai flavors are out of stock. You want to skip those and stop entirly if someone requests a restricted flavor.
Task:-
    1. Skip if flavor is "Out of stock".
    2. Break if flavor is "Discontinued".
"""
# First we will learn continue ->
# Continue -> It will let you continue the iteration in the loop also.
# break -> It will let you completely stop the loop and exit the iteration of it.

# flavors = [
    # "Ginger",
    # "Out of stock",
    # "Mint",
    # "Lemon",
    # "Discontinued",
    # "Black Pepper",
# ]

# for flavor in flavors:
    # if flavor == "Out of stock":
        # continue
    # if flavor == "Discontinued":
        # print(f"{flavor} items found") # this is the if bloack print statement.
        # break
    # print(f"{flavor} items ") # this is the print statement of the for bloack.

# print("Out side of the loop")

staff = [("Adi",19),("Tya",22),("Raj",(23))]
for name, age in staff:
    if age > 18:
        print(f"{name} is alligible to manage the staff")
        break
else:
    print("No one is alligible to manage the staff")