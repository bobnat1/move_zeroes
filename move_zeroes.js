var moveZeroes = function(nums) {
    // start loop to iterate over nums array
    for (i = 0; i < nums.length; i++){
       // if the element in the array equals 0...
        if (nums[i] === 0){
            // copy the element and add it to the end of the array
            nums.push(nums[i])
            // then remove the element from it's current spot in the array
            nums.splice(i, 1)
        }
    }
    return nums
};

nums = [1,0,2,0,3,0,4,0,5]
newArray = moveZeroes(nums)
console.log(newArray)