# Tuples -> They come with round bracket () and are immutable cannot be changed once created.
# Tuples are used to store multiple items in a single variable.

spice_mix = ("Pepper", "Masala", "Leaves")
(spice1,spice2,spice3) = spice_mix
print(f"Spice mix contains: {spice1},{spice2},{spice3}")
red_masala , green_masala = 2,3
print(f"Ratio of red masala R: {red_masala} and G: {green_masala}")
# swapping the values -> 
red_masala , green_masala = green_masala , red_masala
print(f"After swapping R: {red_masala} and G: {green_masala}")
# membership -> This is case sensitive.
print(f"Is leaves in spice mix? {'Leaves' in spice_mix}") # true because leaves is present in the spice_mix tuple.
print(f"Is salt in spice mix? {'Salt' in spice_mix}") # falsse 