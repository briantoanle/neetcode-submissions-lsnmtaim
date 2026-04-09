class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        answer = 0
        start = 0
        for index, char in enumerate(s):
            if char in d and d[char] >= start:
                start = d[char] + 1
            d[char] = index
            answer = max(answer,index - start + 1)
        return answer