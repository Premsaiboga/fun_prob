# sum of prime numbers using functions 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# sum of odd num using functions
def sum_odd(n):
    sum =0
    for i in range(1,n+1):
        if i%2 !=0:
            sum +=i
    return sum

print(sum_odd(10))