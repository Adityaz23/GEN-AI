# What are scopes?
# A scope is a region of a program where a particular variable is accessible in the program.
''' There are 4 types of scopes in Python :-
        1. Local Scope :- It is from the inside the function where the variable is defined.
        2. Enclosing Scope :- It is from the inside the nested function where the variables are defined.
        3. Global Scope :- Top level of the program where the variable is defined .
        4. Built-in Scope :- It is from the built-in function and keywords in Python.
'''

# ! Note :- The scope of a variable is determined by where it is defined in the program.

def serve_chai():
        chai_type = "Masala Chai" # Local Scope
        print(f"Inside the function : {chai_type}")
        
        # Now the variable chai_type is only accessible inside the function serve_chai() and it is not accessible outside the function because it is defined in the local scope of the function.
chai_type = "Ginger Chai"  # Global Scope
print(serve_chai())
print(f"Outside the function :{chai_type}")

# Nested Scope :-
def chai_counter():
        chai_order = "Elaichi Chai" #Enclosing Scope
        print(f"Inside the outer function :{chai_order}")
        def chai_order_count():
                chai_order = "Black Chai" # Local Scope
                print(f"Inside the nested function :{chai_order}")
        chai_order_count()
        # Now i am outside the chai_order_count function 
        print("Outside the nested function: ", chai_order)
        
# Now declaring the global scope variable.
chai_order = "Masala Chai" # Global Scope
chai_counter()
print(f"From the Global Scope : {chai_order}")
# Each function remain uneffected by the variables defined in other functions and they can have their own variables with the same name without any conflict.

''' Global vs Local Scope :- If a variable is defined inside a function, it is local to that function and cannot be accessed outside of it. Where global variables can be accessed from anywhere in the program.'''

# def update_order():
        # chai_type = "Ginger"
        # def kitchen():
                # nonlocal chai_type # This is used to modify the variable defined in the enclosing scope.
                # chai_type = "Masala Chai"
        # kitchen()
        # print(f"Updated order: {chai_type}")
        
chai_type = "Normal Chai"
def front_dek():
    def kitchen():
        global chai_type
        chai_type = "Masala Chai"
    kitchen()

front_dek()

print(f"Final global value of chai type {chai_type}")