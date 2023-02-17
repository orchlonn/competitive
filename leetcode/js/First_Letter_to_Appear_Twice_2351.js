/**
 * @param {string} s
 * @return {character}
 */
 var repeatedCharacter = function(s) {
    let seen = new Set();
    for (const c of s) {
        if (seen.has(c)) {
            console.log(c);
            return c;
        }
        
        seen.add(c);
    }
    
    return " ";
};


repeatedCharacter('asaddv');