from collections import defaultdict

def groupAnagrams(strs):
    # defaultdict is creating the key 
    groups = defaultdict(list)

    # `s` is the order of vowels in strs 
    for s in strs:
        # sorting the `s` and put the value to the key
        key = "".join(sorted(s))
        # the sorted `key` is the key of the group and put the unsorted `s` to that group's value
        groups[key].append(s)
        
    return groups.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))