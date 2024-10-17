def is_prime(n):
    pass# Exercise 1
def is_prime(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6 


    return True

# Test your function
print(is_prime(7))  # Expected output: True
print(is_prime(10))  # Expected output: False