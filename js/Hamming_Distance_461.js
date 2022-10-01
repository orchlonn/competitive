/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */

 var hammingDistance = function(x, y) {
    var num = x ^ y,
    count = 0;
    
    while(num>0){ 

        if( (num &1) == 1) {
            count++;
        }

        num = num>>1;
    }

    return count;
};