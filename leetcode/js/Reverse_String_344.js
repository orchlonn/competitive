/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
 var reverseString = function(s) {
    //  pointer ashiglaj bodson
    var left = 0, right = s.length - 1, tmp ="";
    while(left < right){

        // tmp dotor tvr hadgalah huwisagchaa hiisen
        tmp = s[left];

        // hamgiin ehnii vsgend hamgiin tugsuliin vsgiig hiigeed left ee nemj bna 
        s[left++] = s[right];

        // hamgiin tugsguliin vsgend tmp buyu left index tei vsgvvdiig hiigeed baruunaasaa negiig hasch bna
        s[right--] = tmp;
    }
    // time complexity: 1loop = O(n + m)
    return s;
};