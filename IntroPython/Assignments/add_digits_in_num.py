#add the digits of the num
# e.g: num=13456 output should be 1+3+4+5+6  i.e., 19

num = int(input("Enter any value"))
a=0
num_s=str(num)
for i in num_s:
    a=a+int(i)
print(a)