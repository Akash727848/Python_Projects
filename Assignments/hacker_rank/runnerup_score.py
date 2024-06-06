#Sample Input
#5#23665
#4#1 -1 -2 -1
#5#8 7 6 5 4
#Sample Output
#5

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    print(arr)
    max_num=0
    for i in range(0,len(arr)):
        if arr[i]>=max_num:
            max_num=arr[i]
    arr = [i for i in arr if i != max_num]
    print(arr)
    max_num = 0
    for i in range(0, len(arr)):
        if arr[i] >= max_num:
            max_num = arr[i]
        else:
            max_num=arr[i+1 ]
    print(max_num)
    sorted()
