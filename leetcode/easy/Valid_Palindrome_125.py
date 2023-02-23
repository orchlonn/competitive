import re 
def isPalindrome(s):
    s = re.sub("[^a-zA-Z0-9]+", "", s).lower()
    left = 0
    right = len(s) - 1
    while(left <= right):
        if s[left] != s[right]:
            return False    
        left += 1
        right -= 1
    return True
    
print(isPalindrome(2, '0P'))
