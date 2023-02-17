/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {

    // string dotorh vgnvvdee space eer tasalj awj bna.
    
    // 1. trim function bol vgiin ehend bolon tugsguld bga hooson zaig ustgana.
    // 2. split function bol vgiig space eer tasalj awaad array bolgoj bga
    const arr = s.trim().split(" ");

    // suuliin vgiin urtiig olood return hiij bga.
    return arr[arr.length - 1].length;


    // time complexity -> O(2 * n) => O(n)
    // space complexity -> O(n)
};