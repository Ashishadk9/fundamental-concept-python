# Leap Year Check
# Input
year = int(input("Enter a year:"))
# Check leap year
if(year % 400==0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")