def prime_calc(numb):
    if numb<=1:
        return ""
    for i in range(2,numb):
        if numb%i==0:
            return ""
    return numb
def prime_num(numbers):
    for numb in numbers:
        print(prime_calc(numb))

numbers=list(map(int,input("Enter numbers seperated by comma: ").split(',')))
print(f"Prime numbers are:")
prime_num(numbers)
