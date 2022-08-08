""" Determine if a string is all unique characters. """

# solution with additional data structure - O(n)
def isUnique(str):
    # return is a str has all unique chars
    # make a hash table
    count = {}

    # loop str and fill hash table
    for c in str:
        count[c] = 1 + count.get(c, 0)
       

    for key in count:
        if count[key] > 1:
            return False

    return True


# solution without additional data structure - O(n2)
def isUnique(str):

    # use two for loops to compare characters

    for i in range(0, len(str)):
        char1 = str[i]
        for j in range(i + 1, len(str)-1):
            char2 = str[j]

            if char1 == char2:
                return False
    return True