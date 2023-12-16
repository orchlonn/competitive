/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = (nums) => {
  //  if nums is empty, then return empty array.
  if (nums.length === 0) return [];

  // current element
  let current = nums[0];
  // returning result
  let result = [[current]];

  // added first element, so loop starts with 1
  for (let i = 1; i < nums.length; i++) {
    if (current + 1 === nums[i]) {
      // added element to 2d array
      result[result.length - 1][1] = current + 1;
    } else {
      result.push([nums[i]]);
    }

    current = nums[i];
  }

  return result.map((el) => {
    if (el.length === 1) return String(el[0]);
    else {
      return el.join("->");
    }
  });
};
