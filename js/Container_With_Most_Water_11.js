/**
 * @param {number[]} height
 * @return {number}
 */
 var maxArea = function(height) {
    var  j = 1; maxArea = 0;
    var tmp = j;
    
    for(var i = 0; i < height.length - 1; i++) {
        console.log("print 8 times")
        tmp = j;
        j++;
        console.log(tmp);
        while(tmp < height.length - i - 1){
            
           if(height[i] >= height[tmp]){
              maxArea = height[tmp] * (tmp - i);
               console.log(`max area 1 : ${maxArea}`);
            } else { 
              maxArea = height[i] * (tmp - i);  
            console.log(`max area 2 : ${i}`);
            }
            j++;
        }
    }
    
    return maxArea;
};