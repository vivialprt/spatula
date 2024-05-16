from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Solution with stack and minimization of checks.
        """
        stack = deque()
        stack.append(s)
        # Additional set for checked strings
        seen = set()
        while stack:
            subs = stack.pop()

            for word in wordDict:
                if subs.startswith(word):
                    new_subs = subs[len(word):]
                    if new_subs == '':
                        return True
                    elif new_subs not in seen:
                        stack.append(new_subs)
            seen.add(subs)

        return False


if __name__ == "__main__":
    sol = Solution()
    input_ = (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",  # noqa: E501
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]  # noqa: E501
    )
    output = False
    assert output == sol.wordBreak(*input_)
