# Input 
num = int(input("Enter a number to display the multiplication table:"))
# Check the multiplication table 
print(f"Multiplication table for {num}:")
for i in range(1,11):
    print(f"{num}*{i}={num*i}")