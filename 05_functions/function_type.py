
'''
Type of function :-
        1. Pure vs. Impure
        2. Recursive
        3. anonymous function (in python there are known as lambda function.)
'''

#! 1. Pure functions :-
print("HELLO")
def pure_function(untouch):
        return untouch * 100

''' Not recommended :- And this is the immpure function
total_orders = 0

def impure_chai(cups):
        global total_orders
        total_orders += cups
'''

# Recursive function :- A function which call itself until the condition satisfy it :-(
def mb_protein(n):
        print(n)
        if n == 0:
                return "Protien intake done"
        return mb_protein (n-1) # jab tak n ki value 0 nhi ho jati tab tak chalta rhega je function or agar n ki value change kardi toh wapis se jab tak wo value nhi aa jati tab tk wo hi same process baar baar hoti rhegi.
print(mb_protein(5))

# Lambda function ->

protiein_type = ["whey","impact","isolate", "concentrate", "whey"]
# the lambda have two parameters one is lambda and the second is the iterators. To pass the lambda first args is function name tou can name it anything but you can use anything and filter out anything from the list.
strong_protein = list(filter(lambda protein:protein=="whey",protiein_type))
weak_protein = list(filter(lambda protein:protein!="whey",protiein_type)) 
print(strong_protein)
print(weak_protein)