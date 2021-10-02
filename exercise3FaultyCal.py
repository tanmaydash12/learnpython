#Faulty calculator 
# 45 * 3 = 555 , 56 +9 = 77 , 56/5 = 4

print("Enter 1st variable")
var1 = int(input())
print("Enter 2nd variable")
var2 = int(input())
print("Enter the operator like *  , + , / ")
operatorInCalc = input()

#add
if operatorInCalc == "*":
    if (var1 == 45 and var2 == 3):
        print("result ", 555) 
    else:
        print("result ", var1 * var2)
#mul
elif operatorInCalc == "+":
    if(var1 == 56 and var2 == 9):
        print("result ", 77)
    else:
        print("result", var1+ var2)

#div
elif operatorInCalc == "/":
    if(var1 == 56 and var2 == 6):
        print("result", 4)
    else: 
        print("reult", var1/var2)
else:
    print("You have entered wrong operator ")

