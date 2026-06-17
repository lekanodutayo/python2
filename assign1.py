import logging



logging.basicConfig(level=logging.INFO)


logging.info("Application started")


print("Program is running")







import logging


logging.basicConfig(level=logging.INFO)


username = "mozeed"


logging.info("User %s logged in", username)









def multiply_by_two():
    try:
        
        number = input("Enter a number: ")

        
        number = int(number)

        
        print(number * 2)

    except ValueError:
        
        print("Invalid number entered.")



multiply_by_two()










def divide_numbers():
    try:
        
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        
        result = first_number / second_number

        
        print(result)

    except ZeroDivisionError:
        
        print("Cannot divide by zero.")



divide_numbers()







def greet(name):
    print(f"Hello, {name}!")

greet("Mozeed")








def calculate_area(length, width):
    area = length * width
    return area

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

result = calculate_area(length, width)
print("Area of rectangle:", result)




    


def show_product():
    
    product_name = "Laptop"
    price = 1200

    
    print(f"The {product_name} costs ${price}.")



show_product()









def welcome_user():
    
    name = input("Enter your name: ")

    
    print(f"Welcome, {name}!")



welcome_user()










def calculate_sum():
    
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    
    total = first_number + second_number

    
    print(f"The sum is {total}.")



calculate_sum()





import logging


logging.basicConfig(level=logging.INFO)

def display_user_info():
    logging.info("Program started")

    try:
        
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        
        print(f"Name: {name}, Age: {age}")

        logging.info("User information displayed successfully")

    except ValueError:
        print("Invalid age input.")
        logging.error("Invalid age entered")


display_user_info()