/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {
    var numbers = new Set();
    
    numbers.add(nums)
    for(let item of nums) {
        numbers.add(item)
    }

    for(var i = 0; i <= nums.length; i ++) {
        if(numbers.has(i)){
        } else {
            return i;
        }

    }

};

missingNumber([9,6,4,2,3,5,7,0,1]);