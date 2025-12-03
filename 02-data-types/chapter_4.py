# Boolean =>
is_boiling = True # it is represented as 1 in binary.
is_user_logged_in = False # it is represented as 0 in binary.
stur_count = 5
print(f"Is the water boiling? {is_boiling}") 
print(f"Is the user logged in? {is_user_logged_in}")
total_actions = stur_count + is_boiling + is_user_logged_in # this is known as upcasting.
print(f"Total actions performed: {total_actions}")

have_milk = 0 # 0 and None are one of the false value that we can use in boolean.
print(f"Do we have milk? {bool(have_milk)}")

# Logical Operations in Boolean -> They are basically of three types AND, OR , NOT
have_tea = 1
have_sugar = 1
have_ginger = 1
print(f"Can we make tea? {bool(have_tea and have_sugar)}") # both values must be true, to get the true output.

have_water = False
have_cream = False
can_serve_coffee = have_water or have_cream # only one value must be true to get the true output.
print(f"Can serve coffee? {can_serve_coffee}")