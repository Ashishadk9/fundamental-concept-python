# Prime Number Check
# Input
start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
print("Prime numbers between", start, "and", end, "are: ", end="")

for num in range(start,end+1):
    #prime number are greater than 1
    if num > 1:
        for i in range(2,num):
            # divisible by any number
            if (num % i) == 0:
                # not a prime number
                break
        else:
            # prime number
            print(num,end= "")
            
            