/**
 * @param {number} num
 * @return {number}
 */

 var addDigits = function(num) {
    var isTrue = false;
    var digit;

    if(num != 0){

        while( !isTrue ) {
            while( num >= 10 ){
                var tmp = 0;
                
                tmp = num % 10;
                digit += tmp;
                num = num / 10;
    
                // if( num / 10 > 0 ) {
    
                // } else {
                //     isTrue = true;
                //     return digit;
                // }
            }
               
           num = digit;
           digit = 0;
           if(digit > 10){
               isTrue = true;
           }
       }

    } else {
        return digit;
    }

   return digit;
};