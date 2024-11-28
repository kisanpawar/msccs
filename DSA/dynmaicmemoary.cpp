#include <iostream>
using namespace std;

void allocateAndPrintArray(int size) {
    // Dynamically allocate memory for an array of integers
    int* arr = new int[size];

    // Check if memory allocation was successful
    if (arr == nullptr) {
        cout << "Memory allocation failed!" << endl;
        return;
    }

    // Assign values to the array
    for (int i = 0; i < size; ++i) {
        arr[i] = i + 1;  // Assign some values (1, 2, 3, ...)
    }

    // Print the array elements
    cout << "Array elements: ";
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Deallocate memory for the array
    delete[] arr;
    cout << "Memory deallocated successfully!" << endl;
}

int main() {
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;

    allocateAndPrintArray(size);

    return 0;
}
