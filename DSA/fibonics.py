def fibonacci(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Fibonacci relation
    
    return dp[n]

# Example usage
print(fibonacci(10))  # Output: 55



def knapsack(values, weights, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(values)):
        for w in range(capacity, weights[i] - 1, -1):  # Traverse backwards
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Example usage
values = [60, 100, 120]  # Item values
weights = [10, 20, 30]   # Item weights
capacity = 50            # Knapsack capacity

print(knapsack(values, weights, capacity))  # Output: 220


