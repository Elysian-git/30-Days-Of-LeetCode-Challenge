# SOLUTION 1
# ------------------ O(n * m) TC ----------- O(1) SC --------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]  # assume first word is the prefix

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:  # check if prefix matches start
                prefix = prefix[0 : len(prefix) - 1]  # shrink prefix
                if prefix == "":
                    return ""
        return prefix


# Solution 2
# ------------------ O(n log (n * m)) TC ----------- O(1) SC --------

  class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""                     # store the final prefix
        v = sorted(v)                # sort words lexicographically (dictionary order)
        first = v[0]                 # first string after sorting
        last = v[-1]                 # last string after sorting

        # only need to compare first and last, since they will differ the most
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:  # if chars differ → stop
                return ans
            ans += first[i]          # otherwise, add char to answer
        return ans
