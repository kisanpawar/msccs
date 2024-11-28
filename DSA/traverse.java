public class ArrayTraversal {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        
        // Traditional for loop
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}


public class ArrayTraversal {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        
        // Enhanced for loop (for-each loop)
        for (int element : arr) {
            System.out.println(element);
        }
    }
}



public class ArrayTraversal {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        
        // While loop
        int i = 0;
        while (i < arr.length) {
            System.out.println(arr[i]);
            i++;
        }
    }
}



public class ArrayTraversal {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        
        // Do-while loop
        int i = 0;
        do {
            System.out.println(arr[i]);
            i++;
        } while (i < arr.length);
    }
}



// import java.util.Arrays;

// public class ArrayTraversal {
//     public static void main(String[] args) {
//         int[] arr = {1, 2, 3, 4, 5};
        
//         // Using Streams
//         Arrays.stream(arr).forEach(System.out::println);
//     }
// }

