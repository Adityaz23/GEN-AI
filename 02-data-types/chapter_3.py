# Numbers in the python ->
"""
Integers -> Whole numbers positive and negative both 
Float -> Decimal numbers postivie and negative both
Complex -> Numbers with real and imaginary parts . Ex:- 3+4j
Real -> Numbers with only real parts. Ex :- 2.3 , -2.3
Boolean -> True and False values.
"""

black = 3
ginger = 2.4
total = black+ginger
print(f"Total grams of spice: {total} grams")

remaining = black = ginger
print(f"Reminaing grams of spice: {remaining} grams")

milk = 8
serve_milk = 2
can_Serve = milk/serve_milk # here we will get the decimal value also.
print(f"Can serve milk to: {can_Serve} people")

total_tea = 12
pots = 4
bags_per_pot = total_tea//pots # in this we will get the only whole number value.
print(f"Tea bags per pot: {bags_per_pot} bags")

total_giner = 23
pots_per_cup = 3
remaining_ginger = total_giner%pots_per_cup # this will get the remaining value after division.
print(f"Remaining ginger grams: {remaining_ginger} grams")

base_flavor_strength = 2
scale_factor = 4
powerful_flavor = base_flavor_strength ** scale_factor # this will get the power value. the output is 2*2*2*2*2 = 16.
print(f"Powerful flavor strength: {powerful_flavor}")

total_tea_leaves = 1_00_00_000 # we can use underscore to make the number more readable.
print(f"Total tea leaves available: {total_tea_leaves}")