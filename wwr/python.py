


numberadd = [];
number = 10
while number != 0:
    print("Enter a list of number, type 0 when finished")
    number = int(input("Enter Number: "))
    if number != 0:
        numberadd.append(number)
    elif number == 0:
        
        print (numberadd)
sum = 0

for number in numberadd:
    sum += number
print (sum)

count = len(numberadd)
average = sum / count

print(f"The average is: {average}")

for number in numberadd:
    print(number, end=" ")


        



 

