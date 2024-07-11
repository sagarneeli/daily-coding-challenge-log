class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join([w.lower() for w in s if w.isalnum() or w.isspace()])
        clean_str = "".join(clean_str.split())
        return clean_str == clean_str[::-1]
        