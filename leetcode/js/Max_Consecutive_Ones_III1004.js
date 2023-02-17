/**
 * @param {number[]} nums
 * @return {number}
 */
 var longestOnes = function(nums, k) {
    var left = 0, right = 0, max = 0;

    while(left < nums.length) {

        if(nums[left] == 0) {
            k --;
        }

        if( k < 0) {

            if(nums[right] == 0){
                k += 1;
            }          

            right ++;  
        }

        left++;
    }

    return left - right;
};