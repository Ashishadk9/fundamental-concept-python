#Armstrong Number check
# Input
num=int(input("Enter a numbers:"))
# Calculate the number of digits
order =len(str(num))
# Sum
sum=0
#find the sum of the digits
temp=num
while temp > 0:
    digit=temp % 10
    sum += digit ** order
    temp//=10
#Check the number is Armstrong or not
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")