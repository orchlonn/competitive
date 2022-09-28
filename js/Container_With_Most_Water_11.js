/**
 * @param {number[]} height
 * @return {number}
 */
 var maxArea = function(height) {
     
    var  j = 1; maxArea = 0;
    var tmp = j;
    
    for(var i = 0; i < height.length - 1; i++) {

        tmp = j;
        j++;

        while(tmp < height.length - i - 1){
            
           if(height[i] >= height[tmp]){
              maxArea = height[tmp] * (tmp - i);
            } else { 
              maxArea = height[i] * (tmp - i);  
            }

            j++;
        }
    }
    
    return maxArea;
};