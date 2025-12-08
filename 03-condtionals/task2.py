'''A local cafe wants to show the program suggestion a snack. If a customer asks for the cookies or samosa, it confirms the order. For any other snack, it shows a message that the snack is unavailable.
Task :-
1. Take snack input
2. If it cookies or samosa, confirm the order
3. Else, show "Snack unavailabe"'''

snack = input() # taking the user input for the snack,
print(f"snack: {snack}")
if snack == ' cookie' or snack == 'samosa':
    print(f"Order confirmed for {snack}")
else:
    print(f"Snack unavailable")