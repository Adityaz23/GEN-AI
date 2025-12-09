'''
Docstring for 03-condtionals.task5
You run an online pizza store :
If the order is more than 30$ , delivery is free,
but if the the order is less than 30$ , delivery is 5$
Task:
1. Input: order_amount
2. Use ternary operator to decide delivery fee.
'''
# order_amount = float(input("Enter your order amount: "))
# print(f"Your order amount is: {order_amount}")
# if order_amount > 300:
    # print(f"Your order is: {order_amount} the delivery is free")
# elif order_amount < 300:
    # print(f"Your order is : {order_amount} you will have to pay 5$ for delivery fee")
# else:
    # print(f"Invalid order amount : {order_amount}")
    
    # Now the abother method for the ternary operators for this program -> 
    
order_amount = int(input("Enter the amount: "))
print(f"Your order amount is :{order_amount}")
delivery_fee = 0 if order_amount> 300 else 30
print(f"Your order amount is : {order_amount} so your delivery fee is : {delivery_fee}")