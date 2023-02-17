//! Question: 
// You are given an integer array nums consisting of n elements, and an integer k.
// Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

var findMaxAverage = function(nums, k) {
    let sum = 0;
    for(let i = 0; i < k; i++){
        sum += nums[i];
    }

    let windowSum = sum;

    for(let i = 0; i < nums.length; i++){
        windowSum = windowSum + nums[i + k] - nums[i];
        console.log("window sum : " + windowSum);
        if( windowSum > sum ) {
             sum = windowSum;
        }

    }

    return sum / k;
};