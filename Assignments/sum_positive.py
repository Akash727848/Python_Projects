sume=0
num=int(input("Enter a positive natural number and 0  to quit: "))
while num!=0:
    sume+=num
    num = int(input("Enter a positive natural number and 0  to quit: "))
else:
    print(sume)
print("out of loop")
