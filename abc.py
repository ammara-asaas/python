def add (x,y):
    return x + y
def subtract (x, y):
    return x - y
def multiplay (x, y):
    return x * y
def divied (x,y):
    return x / y
a = False
while a:
    print ("select operation .")
    print ("1.add")
    print ("2. subtract")
    print ("3. multiply")
    print ("4.divied")
    choice = input("Enter choice(1/2/3/4) :  ")
    if choice in ('1', '2' ,'3' ,'4'):
        num1 = float(input("Enter the first nmber: "))
        num2 = float(input("Enter the second number : "))
    if choice == '1':
        print("choice is one")
        print("Result = ",add(num1, num2))
        print(num1, "+", num2, "=", add (num1, num2) )
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2 ))
    elif choice == '3':
        print(num1, "*", num2, "=", multiplay(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divied(num1, num2))
    else:
        print("invaild input")


    








