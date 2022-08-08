""" Determine if one string is a permutation of the other - same characters, but the characters may be in different order. """

def isPermutation(s, n):
    # make hash tables for both strings
    countS, countN = {}, {}

    # edge case for length of strings, they must be the same length to be permutations
    if len(s) != len(n):
        return False

    # loop using string length and populate hash tables with character counts
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countN[n[i]] = 1 + countN.get(n[i], 0)

    # check the keys, if the keys are not same, or the count at key is not same it's not a permutation
    for key in countS:
        if key not in countN:
            return False
        else:
            if countS[key] != countN[key]:
                return False
            
    return True