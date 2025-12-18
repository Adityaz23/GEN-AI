'''
Docstring for 04_loops.prblm5
You are preparing an order summary with customers name and their total bills.
Task :-
    1. Use two lists one for name and one for bills.
    2. Print: "[Name] paid amount [bill]".
'''
name = ["Adit","Tya","Raj","Chirag"]
bills = [2,3,4,5]
# for item in zip(name , bills):
    # print(f"The items are; {item}")
for name, amount in zip(name,bills):
    print(f" {name} paid {amount} dollar")
