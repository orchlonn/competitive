/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
 var merge = function(nums1, m, nums2, n) {
    var i = m + n - 1, m = m - 1, n = n - 1;
     while(n >= 0){
         if(nums1[m] > nums2[n] && m >= 0){
             nums1[i] = nums1[m];
             m--;
         } else{
             nums1[i] = nums2[n];
             n--;
         }
         i--;
     }
     console.log(nums1);
 };