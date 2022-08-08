""" Replace spaces in a string with %20. """

def replaceSpace(str):
    result = ""

    # loop over char and check if it's a space
    for c in str:
        if c == " ":
            result += '%20'
        else:
            result += c

    return result