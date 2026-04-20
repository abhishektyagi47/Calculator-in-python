# Function for add two numbers.
def add(num1,num2):
    return num1 + num2

# Function for subtract two numbers.
def sub(num1,num2):
    return num1 - num2

# Function for multiplication two numbers.
def mul(num1,num2):
    return num1 * num2

# Function for division two numbers.
def div(num1,num2):
    return num1 / num2

# Function for add average numbers.
def avg(num1,num2):
    return (num1 + num2 )/2

print("Please select a operation: \n"
      
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Average")
select=int(input("Please select a operation from 1,2,3,4,5: \n"))

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))


if select==1:
    print(num1, "+" , num2 ,"=",add(num1,num2))
elif select==2:
    print(num1, "-" , num2 ,"=",sub(num1,num2))
elif select==3:
    print(num1, "*" , num2 ,"=",mul(num1,num2))
elif select==4:
    print(num1, "/" , num2 ,"=",add(num1,num2))
elif select==5:
    print("(",num1, "+" , num2,")","/","2" ,"=",avg(num1,num2))
else:
    print("Invalid Operation! Please try again later!")