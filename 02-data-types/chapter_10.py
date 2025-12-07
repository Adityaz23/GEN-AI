# Sets -> Known as for their uniqueness and unordered nature.
essential ={"Python","Java","C++","JavaScript","Rust"}
optional = {"HTML","CSS","Java"}
# Adding the union element of the sets ->

all_lang = essential | optional
print(f"The union of langs are: {all_lang}") # This will print all unique but will not print the repetaion of Java.

# Common elements in bots sets ->
common_lang = essential & optional
print(f"The common elements: {common_lang}") # This will print the common elements in both sets.

# Essentials but not optional ->
diff_lang = essential - optional
print(f"The essential but not optional langs are: {diff_lang}") # This will remove the Java from the both elements of the sets.

# Membership ->
print(f"Is Java is in all langs set? {'Java' in all_lang}") # This will return True as Java is present in both sets.
print(f"Is Ruby is in all langs set? {'Ruby' in all_lang}") # This will return false as Ruby is not present in any of the sets.

