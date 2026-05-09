class Solution:
    #We take each word and parse it with a delimiter
    #but when we do we make sure to use a special delimiter
    #that doest get mixed in with the string
    #so encode will Parse in my program like this
    # len(String):<String>len(String):<String>...
    # doecode will read in the the first two letters and read the string.
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans +=  str(len(s)) + ":"  + s
        return ans
    
    
    
    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+length+1]
            ans.append(word)
            i = j+length + 1
        return ans
