""" Implement a function that merges two sorted lists of m and n elements respectively,

into another sorted list. Name it merge_lists(lst1, lst2). """

def merge_lists(lst1, lst2):
    # set indexes for both lists
    index1, index2 = 0, 0

    # loop while index is less than length of the list
    while index1 < len(lst1) and index2 < len(lst2):
        # check if val in lst 2 is smaller than in lst1, if it is smaller insert it into lst1 at index1
        if lst2[index2] <= lst1[index1]:
            # use insert to insert val into lst1 and index1
            lst1.insert(index1, lst2[index2])
            # move on to the next number
            index1 += 1
            index2 += 1
        else:
            # compare the next val in lst1
            index1 += 1

    # if any remaining items in list 2, extend to list1
    if index2 < len(lst2):
        lst1.extend(lst2[index2:])

    return lst1