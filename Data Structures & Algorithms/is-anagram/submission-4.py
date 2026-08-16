class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabet = [0] * 26

        for i in range(len(s)):
            ss = s[i]
            ts = t[i]
            alphabet[ord(ss) - ord('a')] += 1
            alphabet[ord(ts) - ord('a')] -= 1

        for l in alphabet:
            if l != 0:
                return False

        return True
            