# To declare the variable in pythin we just call that with the name.
# This all are the immutable variables immutable means that the value can be changed.
sugar_amount = 13
print(f"Initialise the sugar level: {sugar_amount}")  # we need to add the f inside the brackets to get the string value or the formal string value.
sugar_amount = 2
print(f"The new value: {sugar_amount}") # we are just changing the refernce not the value.

print(f"This is the id of the sugar amount:  {id(sugar_amount)}")
print(f" 2: {id(2)}")
print(f" 13: {id(13)}")

# This is the id of the sugar amount:  4331956696
 # 2: 4331956696
# 13: 4331957048

# Above we can see that the, address is changed and that is because we are calling it by the reference,