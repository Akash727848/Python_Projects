n=int(input("enter any num: "))
for i in range(0,n):
    print("we should skip5, so the num is: ")
    if i != 5:
        print("\t"+str(i))
        continue
    print("HI")
