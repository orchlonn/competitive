//! [question] => Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

var numSubarrayProductLessThanK = function (nums, k) {
  let ans = 0, left = 0, curr = 1;

  for (let right = 0; right < nums.length; right++) {
    // it is always been worked if curr is less than k element; curr is the multiply of nums[right];
    curr *= nums[right];

    // if k is less than curr element; we need to decrease curr element that is divided by nums[left].
    while (left <= right && curr >= k) {
      curr /= nums[left];
      left++;
    }

    // answer is the indexes of the subarray
    ans += right - left + 1;
  }

  return ans;
};
