#
# ================================================================================
# Noah Mattison     11/10/2023
# Lab 6
# Purpose: Recursion, Searching, and Hashing
# References: educative, geeksforgeeks, code academy, Jude Vargas, Andrew Davison
# ================================================================================

from phonenumbers import *


def binary_search(list1: list, target) -> bool:
    """
    Performs a binary search
    :param list1: list that is being searched
    :param target: value search is looking for
    :return: Boolean
    """
    if len(list1) == 0:
        return False
    # this is a sorted list that has items in it

    first = 0
    last = len(list1) - 1

    # searching through the list
    while first <= last:
        mid = (first + last) // 2
    # decides searching through the first half vs second half
        if target < list1[mid]:
            last = mid - 1
        elif target > list1[mid]:
            first = mid + 1
        else:
            return True
    # if its not in the list, return false
    return False


def sequential_search(list1: list, target) -> tuple:
    """
    Performs a sequential search
    :param list1: list that is being searched
    :param target: value search is looking for
    :return: tuple with a boolean and index
    """
    if len(list1) == 0:
        return False, None

    loc = 0
    while loc < len(list1):
        if target == list1[loc]:
            return True, loc
        else:
            loc += 1
    return False, None


def smart_sequential_search(list1: list, target) -> tuple:
    """
    sequentially search but better!
    :param list1: list that is being searched
    :param target: value search is looking for
    :return: tuple with a boolean and index
    """
    if len(list1) == 0:
        return False, None

    done = False
    loc = 0
    while loc < len(list1) and not done:
        if target <= list1[loc]:
            if loc == len(list1) or target != list1[loc]:
                return False, None
            else:
                return True, loc
        else:
            loc += 1


def recursive_max(list1: list) -> int:
    """
    Function finds the maximum integer in a list
    :param list1: list that is searched through
    :return: maximum integer
    """
    if len(list1) == 1:
        return list1[0]
    else:
        return max(list1[0], recursive_max(list1[1:len(list1)]))


def hash_function(list1: list, item) -> int:
    """
    Function: hash function hashes pretty good
    Args:
        list1: list that is being hashed into
        item: the item being hashed into the list
    Returns: index
    """

    index = item % len(list1)
    beginning = index
    while list1[index] is not None:
        if index == beginning - 1:
            raise ValueError("Stoooop theres no space left")
        index += 1
        if index == len(list1):
            index = 0
    return index


def main():
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(smart_sequential_search([1, 4, 5, 23, 31, 56, 57, 71, 105], 31))
    print(recursive_max([1, 4, 5, 23, 31, 56, 57, 71, 105]))
    hash_list = [None] * 1500
    for item in phone_numbers:
        index = hash_function(hash_list, item)
        hash_list[index] = item
    print(hash_list)


if __name__ == '__main__':
    main()
