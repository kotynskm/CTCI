""" Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t. """

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # use two pointers and search for where chars are not equal
        # if length is same, return substring i + 1 for each is equal
        # if length is different, return s at i, to t i + 1
        # if lengths are different by more than 1 then return false

        # if length of s is greater than t, swap the order
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        # if length diff is > 1 then it's more than 1 edits away
        if abs(len(s) - len(t) > 1):
            return False

        for i in range(len(s)):
            # if letters do not match
            if s[i] != t[i]:

                # if lengths are same
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                # lengths are unequal
                else:
                    return s[i:] == t[i + 1:]
        # only 1 edit away if length of s + 1 equals length of t
        return len(s) + 1 == len(t)