var longestOnes = function(nums, k) {
    var right = 1, ans = 0;     
    for (var left = 0; left < nums.length; left++) {
        var currAns = 0, currK = k;
        while(currK > 0) {

            if(nums[right] == '0'){
                currK --;
                nums[right] == '1';
                right++;
            } else { 
                right++;
            };
        }
        currAns = right - left;
        ans = Math.max(currAns, ans);
        left = right;
        right++;
    }
    return ans; 
};