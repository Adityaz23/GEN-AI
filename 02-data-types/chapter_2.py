# In this chapter we will learn about the mutable variable which means the value we cannot change.

spice_mix = set()
print(f"Intial spice mix id: {id(spice_mix)}")
spice_mix.add("Black Pepper")
spice_mix.add("Ginger")
print(spice_mix) 
spice_mix.remove("Black Pepper")
print(f"This is after removing the black pepper: {spice_mix}") 
print(f"Intial spice mix id: {id(spice_mix)}")


""" Intial spice mix id: 4381710080
Intial spice mix id: 4381710080
{'Black Pepper', 'Ginger'} """
# This is the out put of the above code form the chapter_2 in this the id of the spice_mix variable is same and afeter adding some value to the spice_mix set the id changes. Which means that the variables are mutable.