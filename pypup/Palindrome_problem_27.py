def is_palindrome(s):
    
    left = 0
    right = len(s) - 1    
    
    while right >= 0 and left < len(s) and right > left:    
        if s[left].isalpha():
            left += 1
            continue
        if  s[right].isalpha():
            right -= 1
            continue        
        if s[left]!= s[right].lower:
            return False
        left += 1
        right -= 1
    return True
