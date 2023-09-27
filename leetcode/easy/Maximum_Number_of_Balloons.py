from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    # counting text's every vowel's repetition
    counter = Counter(text)
    # counting balloon word's every vowel's repetition
    balloonCntr = Counter("balloon")
        
    res = len(text)
    # `i` is the order of vowels in balloon ---> "b", "a", "l", "o", "n"
    for i in balloonCntr:
        # counter[i] // balloonCntr[i] means that find the `i` element from counter and balloonCntr then divide 
        res = min(res, counter[i] // balloonCntr[i])
        
    return res


print(maxNumberOfBalloons("balloon"))