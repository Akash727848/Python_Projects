numbers=input("nter values seperated by comma: ").split()
#10 20 23 14 18 18 25
print(numbers)
length=0
for number in numbers:
    length+=1
print(length)
for num in range(0,length):
    numbers[num]=int(numbers[num])
print(numbers)
max_num=0
for num in numbers:
    for i in range(0,length-1):
        if numbers[i]>=numbers[i+1]:
            max_num=numbers[i]
        else:
            max_num=numbers[i+1]
numbers.remove(max_num)
max_num=0
for num in numbers:
    for i in range(0,length-2):
        if numbers[i]>=numbers[i+1]:
            max_num=numbers[i]
        else:
            max_num=numbers[i+1]
print(max_num)