def calci(num1,num2,operator):
    if operator=='+':
        num1+=num2
        return num1
    elif operator=='-':
        num1-=num2
        return num1
    elif operator == '*':
        num1*=num2
        return num1
    else: # operator == '/':
        num1/=num2
        return int(num1)
num1 = int(input("Enter the 1st Number: "))
operator = input("Enter the operation you want:\n+\t-\t*\t/")
num2 = int(input("Enter the 2nd Number: "))
result=calci(num1,num2,operator)
print(result)
another=True
while another:
    next=input("Enter y to continue the calculation\nEnter c for new calculation\nEnter a to exit:\n \t").lower()
    if next=='c':
        num1 = int(input("Enter the 1st Number: "))
        operator = input("Enter the operation you want:\n+\t-\t*\t/\n\t")
        num2 = int(input("Enter the 2nd Number: "))
        result =calci(num1,num2,operator)
        print(result)
        continue
    elif next =='y':
        operator = input("Enter the operation you want:\n+\t-\t*\t/\n\t")
        num2 = int(input("Enter the Next Number: "))
        result=calci(result, num2,operator)
        print(result)
        continue
    else:
        another=False
