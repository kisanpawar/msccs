def lcs(X, Y):
    # Find the lengths of the two sequences
    m = len(X)
    n = len(Y)

    # Create a 2D array to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp array bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the dp table
    lcs_result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Return the LCS as a string
    return ''.join(reversed(lcs_result))

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
result = lcs(X, Y)
print("Longest Common Subsequence:", result)
         
