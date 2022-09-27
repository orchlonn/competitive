/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
 var reverseString = function(s) {
    //  pointer ashiglaj bodson
    var left = 0, right = s.length - 1, tmp ="";
    while(left < right){
        tmp = s[left];
        s[left++] = s[right];
        s[right--] = tmp;
    }
    return s;
};