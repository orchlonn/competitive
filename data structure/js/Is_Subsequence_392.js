/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

//! Question
// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


 var isSubsequence = function(s, t) {
    // i bol t string iin urtaar gvih element, j bol s string iin urtaar gvih element;
    var i = 0, j = 0;
    
    // t vgnii urt bolon s vgnii urtaar gvih while loop.
    while(i < t.length && j < s.length){

        // herwee s vsegnii [j] dahi element vg t vgen dotor bwal j iig 1eer nemj ugnu.
        if(s[j] == t[i]){
            j++;
        }
        
        // t vgnii bvh vsegnvvdeer gvihin tuld [i] iig negeer nemne.
        i++;
    }
    
    // herwee [j] iin urt s vsegnii urrtai tentsvv bwal true gesen vg.
    return j == s.length;
};