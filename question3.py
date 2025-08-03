def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):  # check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# get input from user
num = int(input("Enter an integer: "))

# check and print whether it is prime
print(is_prime(num))
