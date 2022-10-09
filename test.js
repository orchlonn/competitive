/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var findLength = function(nums, k) {
    let left = 0, curr = 0, ans = 0;
    for (let right = 0; right < nums.length; right++) {
        curr += nums[right];
        while (curr > k) {
            curr -= nums[left];
            console.log("curr in while : " + curr);
            left++;
        }
        
        ans = Math.max(ans, right - left + 1);
        console.log("ans : " + ans);
    }

    return ans;
}

// findLength([3, 1, 2, 7, 4, 2, 1, 1, 5], 8);


 var findLength = function(s) {
    let left = 0, curr = 0, ans = 0;
    for (let right = 0; right < s.length; right++) {
        if (s[right] == "0") {
            curr++;
        }
        
        while (curr > 1) {
            if (s[left] == "0") {
                curr -= 1;
            }
            left++;
        }
        
        ans = Math.max(ans, right - left + 1);
    }

    return ans;
}

// findLength("1101100111");
