'''
Docstring for 04_loops.prblm6
You want to simulate oven heating .
It starts with the 40C and goes at the top of 300C
Task:-
    1. Use a while loop .
    2. Incase the temp by 15 until it reaches or exceeds the temp 300
    3. Print each temp step.
'''
temp = 40
while temp <100:
    print(f"It is not heated increase the temprature. {temp} temprature")
    # temp = temp + 15
    temp +=24
    print(f"The temprature reached {temp}")
print(f"Oven is ready to use at {temp} temprature")