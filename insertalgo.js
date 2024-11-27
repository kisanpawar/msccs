function insertionSort(arr) {
    let startTime = performance.now(); // Start time measurement

    for (let i = 1; i < arr.length; i++) {
        let key = arr[i];  // Store current element as key key = 11

        let j = i - 1;      // Initialize j  =  1-0; j = 1


        // Move elements that are greater than the key to one position ahead
        /// is my j >=0 1 >=0  and  arry[1] > 11
        console.log(arr[j] , key)
        while (j >= 0 && arr[j] > key) {
            // main array arr[0 + 1] =  arry[j]   arr[0] = 11

            arr[j + 1] = arr[j];
            // j = j-1
            j = j - 1;
        }
        arr[j + 1] = key;
    }

    let endTime = performance.now(); // End time measurement
    let timeTaken = endTime - startTime; // Time difference

    console.log("Sorted Array:", arr);
    console.log(`Time taken: ${timeTaken.toFixed(10)} milliseconds`);
}



function sortData (arr){

    for(let i= 1; i< arr.length ; i++){

        let  key = arr[i];
        let sortIndex = i - 1;

        while(sortIndex >= 0 && arr[sortIndex] > key){
            arr[sortIndex + 1] = arr[sortIndex];
        
        }





    }


}

// Example usage:
let arr = [12, 11, 13, 5, 6];

/**
 * right to left compare 
 * steps of insert algorithm
 * step1:we start the loop from secound element  of array 
 * pickup element  from the array and store it in a variable( i =  1) --- key =  arr[i];
 * create one variable j =  i - 1




 * 
 */
insertionSort(arr);

