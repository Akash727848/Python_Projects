if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    #5 #10 20 23 14 18 18 25
    #4 #57 57 -57 57 XXXXX this failed
    #10 #6 6 6 6 6 6 6 6 6 5
    max_num=0
    for num in numbers:
        for i in range(0,n-1):
            if numbers[i]>=numbers[i+1]:
                max_num=numbers[i]
            else:
                max_num=numbers[i+1]
    numbers.remove(max_num)
    numbers = [i for i in numbers if i != max_num]
    print(numbers)
    max_num=0
    for_iter=0
    for num in numbers:
        for i in range(0,len(numbers)-1):
            for_iter += 1
            if numbers[i]>=numbers[i+1]:
               max_num=numbers[i]
            else:
               max_num=numbers[i+1]
        else:
            print("for loop done")
    print(max_num)
    print(for_iter)