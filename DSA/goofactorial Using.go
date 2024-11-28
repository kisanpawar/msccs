package main

import "fmt"

// Function to calculate the sum of first n numbers using the formula
func sumOfFirstNNumbers(n int) int {
    return n * (n + 1) / 2
}

func main() {
    var n int
	
    fmt.Print("Enter the value of n: ")
    fmt.Scan(&n)
    
    result := sumOfFirstNNumbers(n)
    fmt.Printf("The sum of the first %d numbers is: %d\n", n, result)
}




package main

import "fmt"

// Recursive function to find the factorial of a number
func factorial(n int) int {
    // Base case: factorial of 0 or 1 is 1
    if n == 0 || n == 1 {
        return 1
    }
    // Recursive case: n * factorial of (n-1)
    return n * factorial(n-1)
}

func main() {
    var n int
    fmt.Print("Enter a number: ")
    fmt.Scan(&n)
    
    // Calculate factorial using the recursive function
    result := factorial(n)
    fmt.Printf("The factorial of %d is: %d\n", n, result)
}
