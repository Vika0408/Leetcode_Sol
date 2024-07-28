class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = [word for word in words if word][::-1]  # To handle multiple spaces
        ans = " ".join(reversed_words)
        return ans
        