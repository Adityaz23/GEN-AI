# Hiding Implementation Details :-
'''You are building a simple app that register users .You want to seprate concerns: getting input , validating it, and saving it :-
Task :-
        Write register_user() function that calls :-
                get_input()
                validate_input()
                save_to_db()
'''
def get_input():
        print("Getting user input :")
        
def validate_input():
        print("Validating the user input :")

def save_to_db():
        print("Saving the user data to the database: ")

def register_user():
        get_input()
        validate_input()
        save_to_db()
        print("User registered successfully!")
register_user()

'''Now, this is for the improving the readability of the code :-
        You sell different types of chai sizes : Instead of writing formulas everywhere , create a function 
        Task :-
        Write calculate_bill(cups,prize_per_cup)
        Return total bill
        Use the function for multiple orders :-
'''
def calculate_bills(cups,price_per_cup):
        return cups * price_per_cup
# The below line is for the returning the value or you can call it like this aswell calulate_bills(2,50) and print the value by storing it in a variable and then printing it.
print(calculate_bills(3,50))

'''Improving Traceability :-
        Your shop adds a 10% VAT to all orders. You want this to be consistent across the whole program and traceable.
        Task :- 
                Write add_vat(price,vat_rate)
                Use it to compute final price for 3 orders.
'''
def add_vat(price,vat_rate):
        return price * (100 + vat_rate)/100
orders = [100,150,200]
for price in orders:
        final_amount = add_vat(price,10)
        print(f" Original Price : {price} , Final price after adding VAT : {final_amount}")