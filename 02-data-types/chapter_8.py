# From this we will learn about the mutable variable which means the value we can change.
# The example of mutable variables are List, Set, Dicitionary.
# List -> They are also just like arrays in other programming language.
ing = ["Lev","Rev","Kev"]
print(f"True string: {ing}")
ing.append("Mev")
print(f"After appending the new value the lise is: {ing}")
ing.remove("Lev")
print(f"After removing the value the list is: {ing}")

# How to join two listts to join two lists we use extend()method.
ing1 = ["Leaves","Keves"]
ing2 = ["Rivers","Lakes"]
ing1.extend(ing2)
print(f"After exteding two lists the new list is: {ing1}")

# using insert() method to insert the value at specific index.
ing1.insert(1, "Beaches")
print(f"After inserting the value at specific index the new list is: {ing1}") # After inserting the value at specific index the new list is: ['Leaves', 'Beaches', 'Keves', 'Rivers', 'Lakes']

ing2.insert(3,"Mountains")
print(f"After inserting the value at specific index at the list ing2 is: {ing2}") # After inserting the value at specific index at the list ing2 is: ['Rivers', 'Lakes', 'Mountains']

# using pop() method to remove the last value from the list.
last_element = ing1.pop()
print(f"After popping the last element from the list the new list is: {ing1}") # After popping the last element from the list the new list is: ['Leaves', 'Beaches', 'Keves', 'Rivers']

# uisng reverse() method to reverse the list.
ing1.reverse()
print(f"After reversing the list ing1 is: {ing1}") # After reversing the list ing1 is: ['Rivers', 'Keves', 'Beaches', 'Leaves']

# using sort() method to sort the list in ascending order.
ing2.sort()
print(f"After sorting the list ing2 is:{ing2}") # After sorting the list ing2 is:['Lakes', 'Mountains', 'Rivers']

# using clear() method to clear the lists.
ing1.clear()
print(f"After clearing the list ing1 is: {ing1}") # After clearing the list ing1 is: []

# using min() and max() method to find the minimum and maximum value from the list.
numbers = [12,31,24,134,3]
print(f"The minimum value from the list is: {min(numbers)}") # The minimum value from the list is: 3
print(f"The maximum value from the list is: {max(numbers)}") # The maximum value from the list is: 134