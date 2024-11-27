public class ArrayTraversal {

    // Function to traverse and print elements of the array
    public static void traverseArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};  // Example array

        // Call the function to traverse and print the array
        traverseArray(arr);
    }
}
