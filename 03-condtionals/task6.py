"""
Docstring for 03-condtionals.tak6
You are building a ticket info system for railway app.
Based on seat type, show its feature :-
1. Input : 'sleeper' ,'General', 'AC', 'Luxury'
2. Match using match case.
3. Unknown : Show -> "Invalid seat type."
"""

input_seat = input("Enter seat type: Choose from Sleeper/AC/General/Luxury: ").lower()
match input_seat:
    case "sleeper":
        print("Sleeper - No AC but beds are available.")
    case "sC":
        print("AC fully air consitioned")
    case "general":
        print("General not full berth")
    case "luxury":
        print("Will get a peresonal attendant")
    case _:
        print("Invalid seat types.")