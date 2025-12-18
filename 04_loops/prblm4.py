'''
Docstring for 04_loops.prblm5
    You're creating a tea menu board each item in the board must be numbered.
    Task: Use the enumerate() to print the menu items with numbers.
'''
menu = ["Green","Black","Lemon","Spiced","Mint"]
for idx,item in enumerate(menu,start=1):
    print(f"The menu from the items are {idx} : {item} tea")