numbers=[]
b=[]
for i in range(4x   ):
    number = int(raw_input("Enter a number or press 'Enter' to finish:"))
    if not number:
        break
    numbers.append(number)
sumOfNumbers= sum(numbers)
average = sumOfNumbers/len(numbers)
numbers.sort()
print "Count =",len(numbers),
print "Sum of all numbers is: ",sumOfNumbers,
print "Average of all the numbers is: ",average,
print "The smallest number is : ",numbers[0],
print "The largest number is: ",numbers[len(numbers)-1]

