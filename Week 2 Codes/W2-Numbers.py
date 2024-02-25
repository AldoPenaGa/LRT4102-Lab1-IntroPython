numbers = [0, 1,2,3,4,5,6,7,8,9,12,20]

sumEven = 0
counterEven = 0
productOdd = 1

for i in numbers:
    test = i%2
    if test == 0:

        numType = "even"
        sumEven = sumEven + i
        counterEven +=1
        avgEven = sumEven / counterEven
    
    else:
        numType = "odd"
        productOdd = productOdd * i

print("The average of the even numbers is: " + str(avgEven))
print("The product of the odd numbers is: " + str(productOdd))


