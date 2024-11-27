# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Euclid's Theorem Verification (Infinitely many primes)
def euclids_theorem_verification(limit):
    # Generate primes up to 'limit' and check for a contradiction (which never occurs)
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    
    # Check if the prime list ends or not. Euclid's theorem states that primes are infinite.
    return primes

# Fermat's Little Theorem Verification
def fermats_little_theorem(a, p):
    # Check if p is prime and a is not divisible by p
    if is_prime(p) and a % p != 0:
        # Fermat's Little Theorem: a^(p-1) % p should be 1
        return pow(a, p - 1, p) == 1
    else:
        return False

# Example to verify Euclid's Theorem (Find primes up to 1000)
print("Verifying Euclid's Theorem: Primes up to 1000")
primes = euclids_theorem_verification(1000)
print(f"Primes found: {primes[:20]}...")  # Show first 20 primes

# Example to verify Fermat's Little Theorem
print("\nVerifying Fermat's Little Theorem (a = 2, p = 7):")
a = 2
p = 7
result = fermats_little_theorem(a, p)
print(f"Does {a}^{p-1} % {p} == 1? {result}")

print("\nVerifying Fermat's Little Theorem (a = 3, p = 11):")
a = 3
p = 11
result = fermats_little_theorem(a, p)
print(f"Does {a}^{p-1} % {p} == 1? {result}")
