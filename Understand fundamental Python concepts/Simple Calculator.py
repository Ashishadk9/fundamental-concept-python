print("Welcome to the Simple Calculator!")
# get two numbers from the user
num=float(input("Enter first number: "))
num1=float(input("Enter second number: "))
# Show options
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
# Choice input
choice=input("Enter choice (1-6):")
# Do the math based on the choice
if choice == '1':
    result = num + num1
    print(f"{num} + {num1} = {result}")
elif choice == '2':
    result = num - num1
    print(f"{num} - {num1} = {result}")
elif choice == '3':
    result = num * num1
    print(f"{num} * {num1} = {result}")
elif choice == '4':
    if num1 != 0:
        result = num / num1
        print(f"{num} / {num1} = {result}")
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print("Invalid choice. Please select(1-4).")