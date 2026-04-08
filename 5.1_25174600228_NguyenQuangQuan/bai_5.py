def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

n = int(input("Nhập n: "))
numbers = list(range(1, n + 1))

primes = [x for x in numbers if is_prime(x)]
perfects = [x for x in numbers if is_perfect(x)]

print("Số nguyên tố:", primes)
print("Số hoàn hảo:", perfects)