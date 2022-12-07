print("enter the first num")
a = input()
print("enter the second num")
b = input()
print("choose the operator: \n 1- (+) \n 2- (-) \n 3- (*) \n 4- (/) \n 5- (%)")
operator = int(input())
if operator == 1:
    sum = int(a) + int(b)
    print("the addition of  " + a + " + " + b + " is: " + str(sum))
elif operator == 2 :
    substraction = int(a) - int(b)
    print("the substraction of  " + a + " - " + b + " is: " + str(substraction))
elif operator == 3 :
    multiplication = int(a) * int(b)
    print("the multiplication of  " + a + " * " + b + " is: " + str(multiplication))
elif operator == 4 :
    devision = int(a) / int(b)
    print("the devision of  " + a + " / " + b + " is: " + str(devision))
elif operator == 5 :
    modulo = int(a) % int(b)
    print("the modulo of  " + a + " % " + b + " is: " + str(modulo))
else :
    print("operation not found")