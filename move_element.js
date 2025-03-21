var moveZeroes = function(nums, element) {
    // start loop to iterate over nums array
    for (i = 0; i < nums.length; i++){
       // if the element in the array equals to...
        if (nums[i] === element){
            // copy the element and add it to the end of the array
            nums.push(nums[i])
            // then remove the element from it's current spot in the array
            nums.splice(i, 1)
        }
    }
    return nums
};

nums = [
    34, null, 87, 21, 56, null, 12, 98, 45, 67, 
    89, 23, null, 78, 90, 32, null, 47, 53, null, 
    71, 29, 10, 95, null, 64, 38, 27, null, 99, 
    84, 16, null, 42, 59, 3, 88, null, 77, 11, 
    20, 36, 61, null, 72, 81, 5, 50, null, 68, 
    40, 14, 93, 25, 7, null, 55, 31, 44, 62, 
    null, 80, 97, 66, 35, 18, 22, null, 52, 41, 
    58, null, 79, 92, 9, 26, 48, null, 13, 86, 
    46, 73, 2, null, 30, 100, 6, 70, 63, 37, 
    null, 33, 57, 82, 51, 4, 28, null, 96, 1
  ]
  
newArray = moveZeroes(nums, null)
console.log(newArray)