# Reducing the code duplication :-
''' Write a function called print_order(name,chai_type) , call it mutliple times for different names and chai types :-
def print_order(name,chai_type,age):
        print(f"{name} ordered {chai_type} and is {age} years old")
print_order("Aman", "Masala Chai", 23)
print_order("Riya", "Zero Sugar Chai", 24)
print_order("Raj", "Black Chai", 25)
print_order("Aditya", "Elaichi Chai", 26)
print_order("Roy", "Ginger Chai", 27)
# print(print_order)
'''


'''You are creating a monthly report for a cafe's sales. Instead of putting all logic at one place break it down into functions :-
        1. Write a function called generate_report() that calls .
                fetch_sales()
                filter_valid_orders()
                summarize_data()
'''
def fetch_sales():
        print("Fetching the sales data: ")

def filter_valid_orders():
        print("Filtering the valid orders: ")

def summarize_data():
        print("Summarizing the sales data: ")

def generate_report():
        fetch_sales()
        filter_valid_orders()
        summarize_data()
        print("Report generated successfully!")
generate_report()