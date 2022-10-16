/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
    
    let longArrComplete = nums.length;
    
    // Borramos los duplicados
    const deleteDuplicates = new Set(nums);
    nums = Array.from(deleteDuplicates);
    
    let longArrDelete = nums.length;
    let push = longArrComplete - longArrDelete;
    
    for(let i = 0; i <= push; i++){
        nums.push("_");
    }
    
    return longArrDelete;
    
    
};