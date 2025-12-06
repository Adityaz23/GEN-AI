# Operations on lists and bytearrays.
base_liq = ["Lemon","Gin","Sugar"]
edit_liq = ["Masala","Ice"]
all_liq = base_liq + edit_liq
print(all_liq) # ['Lemon', 'Gin', 'Sugar', 'Masala', 'Ice']
strong_liq = ["vodka", "Rum"] * 4
print(f"Strong liquor List: {strong_liq}")
sorted_liq = sorted(all_liq)
print(f"Sorted Liquor List: {sorted_liq}")
raw = bytearray(b"Whiskey")
print(f"Raw byte array: {raw}")
raw_drink = raw.replace(b"skey",b"Scotch")
print(f"Raw byte array: {raw_drink}")

