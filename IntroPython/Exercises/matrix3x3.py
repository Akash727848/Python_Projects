l = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
m = list(input("enter the index1: "))
m[0] = int(m[0])
m[1] = int(m[1])
l[ m[0] - 1][ m[1] - 1]='x'
print(f"The final matrix is:\n{l[0]}\n{l[1]}\n{l[2]}")


