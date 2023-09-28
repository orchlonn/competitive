def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # create the counter for ransomNote
    rnCntr = Counter(ransomNote)
    # create the counter for magazine
    magazineCntr = Counter(magazine)
    # creata a list for keys that will be used in remove section
    keys_to_remove = []

    # loopnig for magazine length
    for i in magazineCntr:
        # looping for ransomNote
        for k in rnCntr:
            # checking that if there is an any `i`th element in ransomNote
            if i == k:
                # checking that `i`th element of magazine is greater or not than ransomNote
                if magazineCntr[i] >= rnCntr[k]:
                    # if greater put the key to the list
                    keys_to_remove.append(k)
                    
    # delete all the keys from array
    for key in keys_to_remove:
        del rnCntr[key]
    # if list is empty return true, else not
    return True if len(rnCntr) == 0 else False