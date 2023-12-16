var findMaxConsecutiveOnes = function(nums) {
    let output = 0;
    let count = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) {
            count++;
        } else {
            output = Math.max(output, count);
            count = 0;
        }
    }
    
    return Math.max(output, count);
};