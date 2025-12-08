# You are going to create a notification system for a smart kettle. It should remind the user only when the kettle has finished boiling .Task :-
# 1. A variable kettle_boiled = True
# 2. If boiled, show: "Kettle done! Time to boil eggs."

kettle_boiled = input() # taking the user input.
print(f"kettle boiled: {kettle_boiled}")
kettle_boiled = kettle_boiled == 'True' 
if kettle_boiled:
    print(f"Kettle done! Time to boil eggs.")
else:
    print(f"Kettle is still boiling.")