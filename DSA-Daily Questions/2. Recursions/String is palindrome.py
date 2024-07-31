def isPalindrome(string: str) -> bool:
    def reverse(string: str, i) -> bool:
        n = len(string)
        if i >= n // 2:
            return True
        if string[i] != string[n - i - 1]:
            return False
        return reverse(string, i + 1)

    return reverse(string, 0)


###leet code string plaindrome

import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        rev_s = s[::-1]

        if s == rev_s:
            return True
        else:
            return False


class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
