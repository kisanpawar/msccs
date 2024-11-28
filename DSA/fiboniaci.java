public class Fibonacci {

    public static int fibonacci(int n) {
        if (n <= 1) return n;
        
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2]; // Fibonacci relation
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int n = 10; // Example: Find the 10th Fibonacci number
        System.out.println(fibonacci(n)); // Output: 55
    }
}

// dynamic


public class Knapsack {

    public static int knapsack(int[] values, int[] weights, int capacity) {
        int n = values.length;
        int[] dp = new int[capacity + 1];

        for (int i = 0; i < n; i++) {
            for (int w = capacity; w >= weights[i]; w--) {  // Traverse backwards
                dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
            }
        }
        return dp[capacity];
    }

    public static void main(String[] args) {
        int[] values = {60, 100, 120};  // Item values
        int[] weights = {10, 20, 30};   // Item weights
        int capacity = 50;              // Knapsack capacity
        
        System.out.println(knapsack(values, weights, capacity)); // Output: 220
    }
}
