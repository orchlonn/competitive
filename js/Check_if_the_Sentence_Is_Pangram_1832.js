/**
 * @param {string} sentence
 * @return {boolean}
 */
 var checkIfPangram = function(sentence) {
    //  create set algorithm
    let alphabet = new Set();

    // Add first element due to if I add first element in the for 
    // loop, I can't compare my first element with other elements.
    alphabet.add(sentence[0]);

    // added the first element directly so initial value of counter is 1.
    var counter = 1;
    for(var i = 1; i < sentence.length; i++) {
        // Checks the element is overlaped or not.
        if(alphabet.has(sentence[i])){
            // if it overlaps remove the i-th element.
            alphabet.delete(sentence[i]);

            // decrease counter
            counter --;
        }

        // always add i-th element to set alogrithm.
        alphabet.add(sentence[i]);

        // increace the counter.
        counter ++;
    }
    if(counter === 26) {
        return true;
    } else {
        return false;
    }
};

checkIfPangram("thequickbrownfoxjumpsoverthelazydog");