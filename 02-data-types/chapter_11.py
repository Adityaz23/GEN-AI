 # Dictionary -> To call the dictionary we us dict() method.
drink = dict(type = "Cocktail", name = "Mojito", ingredients = ["Rum","Mint","Lime"], size = "Medium")
print(f"drink order: {drink}")

poha_recipe = {} # using the empty curly braces to create an empty dictionary.
poha_recipe["type"] = "Breakfast"
poha_recipe["name"] = "Poha"
poha_recipe["ingredients"] = ["Rice flakes","Onion","Peanuts","Spices"]
print(f"Poha Recipe: {poha_recipe}") # this will print the whole dictionary.
print(f"Poha Ingredients: {poha_recipe['ingredients']}") # this will print only the ingredients of the poha recipe. Poha Ingredients: ['Rice flakes', 'Onion', 'Peanuts', 'Spices']

del poha_recipe["type"] # using del keyword to delete the specific key value pair from the dictionary.
print(f"After deleting the type key the new poha recipe is: {poha_recipe}") # After deleting the type key the new poha recipe is: {'name': 'Poha', 'ingredients': ['Rice flakes', 'Onion', 'Peanuts', 'Spices']}
# Memebership test in dictionary ->
print(f"Is peanuts is in the ingredients? {'Peanuts' in poha_recipe['ingredients']}") # Is peanuts is in the ingredients? True

roti_recipe = {"type":"Lunch", "name":"Roti","ingredients":["Wheat flour","Water","Salt"],"size":"Medium"}
print(f"Order details (keys): {roti_recipe.keys()}") # Order details (keys): dict_keys(['type', 'name', 'ingredients', 'size'])
print(f"Order details (values):{roti_recipe.values()}") # Order details (values):dict_values(['Lunch', 'Roti', ['Wheat flour', 'Water', 'Salt'], 'Medium'])
print(f"Order details (items): {roti_recipe.items()}") # Order details (items): dict_items([('type', 'Lunch'), ('name', 'Roti'), ('ingredients', ['Wheat flour', 'Water', 'Salt']), ('size', 'Medium')])
last_order = roti_recipe.popitem()
print(f"Removed last order item: {last_order}") # Removed last order item: ('size', 'Medium') this will print the last items key value pair from the dictionary.
added_order = roti_recipe.update({"calories":"200"})
print(f"After adding the new key value pair the order is : {roti_recipe}") # After adding the new key value pair the order is : {'type': 'Lunch', 'name': 'Roti', 'ingredients': ['Wheat flour', 'Water', 'Salt'], 'calories': '200'}
extra_item = {"drink":"Manog Lassi", "dessert":"Ras Malai"}
print(f"Extra items to add: {extra_item}")
print(f"Updated order with extra items: {roti_recipe | extra_item}") # Updated order with extra items: {'type': 'Lunch', 'name': 'Roti', 'ingredients': ['Wheat flour', 'Water', 'Salt'], 'calories': '200', 'drink': 'Manog Lassi', 'dessert': 'Ras Malai'}
# or we also have another method called update() method to update the ductionary with another dictionary.
roti_recipe.update(extra_item)
print(f"After updating the roti recipe with extra items the new order is: {roti_recipe}") # After updating the roti recipe with extra items the new order is: {'type': 'Lunch', 'name': 'Roti', 'ingredients': ['Wheat flour', 'Water', 'Salt'], 'calories': '200', 'drink': 'Manog Lassi', 'dessert': 'Ras Malai'}
how_poha_recipe = poha_recipe.get("ingredients","No note") # This will get the value of the key ingredients from the poha_recipe.
print(f"Getting the name of the poha recipe using get() method: {how_poha_recipe}") # Getting the name of the poha recipe using get() method: ['Rice flakes', 'Onion', 'Peanuts', 'Spices']