# Boolean =>
is_boiling = True # it is represented as 1 in binary.
is_user_logged_in = False # it is represented as 0 in binary.
stur_count = 5
print(f"Is the water boiling? {is_boiling}") 
print(f"Is the user logged in? {is_user_logged_in}")
total_actions = stur_count + is_boiling + is_user_logged_in # this is known as upcasting.
print(f"Total actions performed: {total_actions}")