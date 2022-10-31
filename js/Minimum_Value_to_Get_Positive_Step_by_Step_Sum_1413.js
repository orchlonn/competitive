/**
 * @param {number[]} nums
 * @return {number}
 */
 var minStartValue = function(nums) {
    var isPassed = false, output = 1;
    while(isPassed == false) {
        var tempSum = output;
        var counter = 0;

        for(var i = 0; i < nums.length; i++){
            tempSum += nums[i];
            if(tempSum >= 1){
                counter++;
            }
        }
        if(counter === nums.length) {
            // console.log(counter , " counter in length ", nums.length);
            isPassed = true;
            break;
        }
        output ++;

    }
    console.log(output);
    return output;
};


minStartValue([1,-2,-3]);