 Given a string s consisting of words and spaces, return the length of the last word in the string.
 A word is a maximal substringconsisting of non-space characters only.





class Solution:
    def lengthOfLastWord(self,s: str) -> int:
        return len(s.split()[-1])
    
