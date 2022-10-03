/**
 * @param {number[]} height
 * @return {number}
 */

const maxArea = (height) => {

	var max = 0;

	// first pointer
	for(var i = 0; i < height.length; i++) {

		// second pointer
		for(var j = 0; j < height.size; j++) {

			// find area between first and last pointers.
			var currentArea = Math.min(height[i], height[j]) * (j - i);
			// compare current areas.
			max = Math.max(max, currentArea);
		}

	}

	return max;
};

// Time complexity: O(n * m);
// space complexity: O(1);
