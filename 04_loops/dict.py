# Defining dictionary ->
users = [
    {"id": 1,"total": 200, "coupon": 200},
    {"id": 2,"total": 300, "coupon": 100},
    {"id": 3,"total": 100, "coupon": 300}
]
# using discounts as a dictionary -> 
discounts = {
    100: (0.2, 0), 
    200: (0.3, 0),
    300: (0, 40)
}
for user in users:
    percent, fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    # print(f"The total value is: {discount}")
    print(f"{user['id']} paid {user["total"]} and got only {discount}")