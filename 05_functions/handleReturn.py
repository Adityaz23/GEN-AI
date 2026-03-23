print("Hello")
print("Hello from the handle return arguments file")

# def make_app():
        # return "Here is your 100,000$ app."
        # print("Dekh le khud hi")
# Whenever writing a function you need to return the statement not print it cause then the value of the print statement will always be none whatever you pass on that variable.
# print (make_app()) no easy to understand
# Here we are using the another variable to store the return value and then printing it,
# return_value = make_app()
# print(return_value)

def antinationals(**names):
        print("List of names")
        print(names)
        return "These are the name of some anti nationals"
antinationals(person1="Dhruv",person2="Rant", person3="Desh")

def gym_status(creatine_taken):
        if creatine_taken == 0:
                return "Khel khatam bete"
        return "Body pump hai"
print(gym_status(0)) # agar 0 akele pass karoge toh kuch nhi print hoga iteration bas pehle return tak hi jayega.
print(gym_status(5)) # agar 0 ke alawa koi bhi value pass karoge toh fir tumhara return jitne bhi ho sab pass hoyrnge.

def epstien_report():
        return "JEFF" , 1 # names and member
name , member = epstien_report()
print("Name: ",name)
print( "Member: ", member)
print(epstien_report())