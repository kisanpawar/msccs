#include <stdio.h>

// Function to convert Celsius to Fahrenheit
float celsius_to_fahrenheit(float celsius) {
    return (celsius * 9/5) + 32;
}

// Function to convert Fahrenheit to Celsius
float fahrenheit_to_celsius(float fahrenheit) {
    return (fahrenheit - 32) * 5/9;
}

int main() {
    float celsius, fahrenheit;

    // Input temperature in Celsius
    printf("Enter temperature in Celsius: ");
    scanf("%f", &celsius);
    fahrenheit = celsius_to_fahrenheit(celsius);
    printf("%.2f°C is equal to %.2f°F\n", celsius, fahrenheit);

    // Input temperature in Fahrenheit
    printf("Enter temperature in Fahrenheit: ");
    scanf("%f", &fahrenheit);
    celsius = fahrenheit_to_celsius(fahrenheit);
    printf("%.2f°F is equal to %.2f°C\n", fahrenheit, celsius);

    return 0;
}
