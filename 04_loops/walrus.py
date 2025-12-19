'''
Docstring for 04_loops.walrus

'''

# First we will write our code without the walrus operator ->
# value = 13
# remiander = value % 2
# if remiander:
#     print(f"The remainder for the {value} is {remiander}")
    
# Now the walrus operator is that which we can directly render in the if statement as well as in the for loop =>

number = 12
if (last := number % 5):
    print(f"The last digit of the number is {number}")
else:
    print(f"The number {number} is fully divisible")
    
available_size = ["Large","Medium","Small"]
if(requested_size := input("Enter you size: ").lower()) in (
    requested_size.lower() for requested_size in available_size
):
    print(f"The size which the user entered is {requested_size} and is available in: {requested_size}")
    
flavors = ["masala","ginger","lemon","mint"]
print(f"The availabe flavors are: {flavors}")
while (flavor := input("Choose your flavor: ").lower()) not in (flavor.lower() for flavor in flavors):
    print(f"The flavor {flavor} is not available")
print(f"The flavor is available: {flavor}")
