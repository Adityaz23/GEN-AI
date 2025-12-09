"""Now we will generate a tea stall where different prices for different cup sizes. Write a program that calculates the price based in size.
1. Input : 'small' 'medium' 'large'
2. Small : 10$ , Medium : 15$ , Large : 20$
3. If invalid show :'Unavailable cup size.'
"""

chai_order = input("Choose your cup size: small/medium/large: ").lower()
if chai_order == "small":
    print(f"Your cup size is {chai_order} please pay 10$ for it.")
elif chai_order == "medium":
    print(f"Your cup size is {chai_order} please pay 15$ for it.")
elif chai_order == "large":
    print(f"Your cup size is {chai_order} please pay 20$ for it.")
else:
    print("Your cup size is unavailable")