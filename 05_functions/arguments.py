print("Hello World from the arguments in the functions file")
name = input("Enter your name: ")
print(f"Hello {name}, Welcome to the world of the functions in Python")

chai_type = "Ginger "
def prepare_chai(orders):
        print(f"Preparing {chai_type}")
prepare_chai(chai_type)
print(chai_type)
chai_type = [1,2,3,4]
def edit_chai(cup):
        cup[1] = 10
edit_chai(chai_type)
print(chai_type)

# the positioning ig the arguments :-
def make_chai(tea,milk,sugar):
        print(tea,milk,sugar)
make_chai("Assam","Yes","Low") # this is positional cause we know what value is at what position at the parameters.
# The below one is the keywords arguments.
make_chai(tea="Black",milk="Cow",sugar="Low")

# so the first one is for the ing and the second one is for the extra entry . The * icon stores as the tuple and the ** stores as the dictionary.
'''Ingredients:  ('Ginger', 'Black Pepper')
Extras:  {'sweetner': 'Honey', 'foam': 'yes'}'''

def special_chat(*ingredeints, **extras):
        print("Ingredients: ",ingredeints)
        print("Extras: ", extras)
special_chat("Ginger","Black Pepper",sweetner="Honey", foam="yes")
        
def chat_masala(*material, **sauce):
        print("Materials: ", material)
        print("Sauces: ",sauce)
chat_masala("Aloo","Chole", green_sauce="Pudina", red_sauce="Imli")
