def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def check_prime_numbers(numbers):
    for num in numbers:
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

# Example usage:
given_numbers = map(int,input("Enter numbers seperated by comma: ").split(','))
check_prime_numbers(given_numbers)
