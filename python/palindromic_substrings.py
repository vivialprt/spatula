"""
Solutions for Palindromic Substrings problem
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Solution by expanding from center.
        Expanding happens twice, for oddly-length palindromes
        and for evenly-length palindromes.
        Each expantion happens while
        """
        count = 0
        for center in range(len(s)):
            # Expanding for oddly-length palindromes
            amplitude = 1
            while (
                center - amplitude >= 0
            ) and (
                center + amplitude < len(s)
            ) and (
                s[center - amplitude] == s[center + amplitude]
            ):
                amplitude += 1
            count += amplitude

            # Expanding for evenly-length palindromes
            amplitude = 0
            while (
                center - amplitude >= 0
            ) and (
                center + amplitude + 1 < len(s)
            ) and (
                s[center - amplitude] == s[center + amplitude + 1]
            ):
                amplitude += 1
            count += amplitude

        return count


if __name__ == "__main__":
    sol = Solution()
    answer = sol.countSubstrings("aaa")
    assert answer == 6
