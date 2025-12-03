# String -> A squence of characters enclosed in single or double quotes. Strings are immutable.
# Strings have three main parts -> 1. Core 2. Indexing 3. Slicing

greeting = "Hello,"
customer_name = 'Aditya'
print(f"Greeting message: {greeting}Aditya")
full_greeting = greeting + " " + customer_name + "!" 
print(full_greeting)
fullName = "Aditya Kumar Soni"
print(f"Letters of the name: {fullName[0:5:2]}") # this will print the letters from index 0 to 5 with a step of 2.
print(f"Letters: {fullName[1:]}") # this will skip the first letter and print the rest of the string.
print(f"Reversed Name: {fullName[::-1]}") # this will print the string in reverse order.

label_text = "Aditÿa" # this is a string with the special character it will cause isssude while enoding: b'Adit\xc3\xbfa'
encode_text = label_text.encode("utf-8") # this will encode the string into bytes using utf-8 encoding.
print(f"Encoded text: {encode_text}")
decoded_label = encode_text.decode("utf-8") # this will decode the bytes back into string.
print(f"Decode text: {decoded_label}") # Aditÿa