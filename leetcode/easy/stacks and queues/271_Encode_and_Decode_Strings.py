class Solution:

    def encode(self, strs: List[str]) -> str:
        # 1. get a length of a single element of the list
        # 2. put the length and pound symbol before the word
        encoded_str = ''
        for w in strs:
            encoded_str += str(len(w)) + "#" + w
        
        # 3. make it an one list
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_arr = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1 
            j = i + length
            decoded_arr.append(s[i:j])
            i = j
            
        return decoded_arr
