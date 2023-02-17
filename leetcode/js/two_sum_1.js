/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let dic = new Map();
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let complement = target - num;
        if (dic.has(complement)) {
            return [i, dic.get(complement)];
        }
        
        dic.set(num, i);
    }
    return [-1,-1];
};


twoSum([2,7,11,15], 0);