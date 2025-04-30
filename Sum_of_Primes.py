def sum_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not primes

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False

    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

# Calculate sum of all prime numbers up to 2 million
limit = 2_000_000
result = sum_primes(limit)
print(f"Sum of all primes below {limit} is: {result}")
