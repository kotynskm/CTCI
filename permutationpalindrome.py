""" Check if a str is a permutation of a palindrome. A palindrome is a word spelled the same forwards and backwards. A permutation
 
 is a rearrangement of the letters. """

def is_palin_perm(str):
    # first remove white space and convert to lower case
    chars_dict = {}
    odds_count = 0
    input_str = str.replace(" ", "")
    input_str = input_str.lower()

    # make a hash table of the characters in the str
    for c in input_str:
        chars_dict[c] = 1 + chars_dict.get(c, 0)

    # loop through keys and check the values for odds, increment odds count and check if odds count != 0
    for key in chars_dict:
        if chars_dict[key] % 2 != 0:
            odds_count += 1
        elif chars_dict[key] % 2 != 0 and odds_count != 0:
            return False
    return True



