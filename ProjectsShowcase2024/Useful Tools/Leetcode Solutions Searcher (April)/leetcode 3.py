class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        subString = ''
        for i in range(len(s)):
            char = s[i]
            print(char)
            if char in hm.keys():
                index = i
                print(index)
                subString = s[:index]
                print(subString)
                break
            else:
                hm[char] = 1
        return len(subString)