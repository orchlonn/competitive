/**
 * @param {number[]} height
 * @return {number}
 */

const maxArea1 = (height) => {

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





// improved performance 

const maxArea2 = (height) => {
	
	var max = 0, left = 0, right = height.length - 1;

	while(left < right) {
		var curretnArea = Math.min(height[left], height[right]) * (j - i);

		max = Math.max = Math.max(max, curretnArea);

		if(height[left] < height[rihgt]) {
			left++;
		} else {
			right--;
		}

	}

	return max;

};