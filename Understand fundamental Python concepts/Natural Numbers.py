# sum of Natural Numbers
# Input
n =int(input("Enter a positive integer:"))
# Check if the number is positive
if n<1:
    print('Check the number is positive')
else:
    # Calculate sum
    sum = n*(n + 1) // 2
    # Display the result
    print('The sum of the first', n, 'natural numbers is:', sum)