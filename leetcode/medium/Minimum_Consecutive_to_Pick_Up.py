def minimumCardPickup(self, cards: List[int]) -> int:
    # declares a int defaultdict dictionary
    dic = defaultdict(int)
    # declares a infinite float number for min
    ans = float("inf")

    # looping for all items in cards
    for i in range(len(cards)):
            
        # checking that an elements exists in the dictionary
        if cards[i] in dic:
            # if the elements exists, do minus from last index to first index
            ans = min(ans, i - dic[cards[i]] + 1)
                
        # if not exists put it to the dictionary. BTW, the value is the key of an dictionary
        dic[cards[i]] = i

    # if we do have ans return the answer, if not return -1
    return ans if ans < float("inf") else -1