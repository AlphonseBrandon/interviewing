"""
Author: Alphonse Brandon
Date Created: 11/11/2024 12:00
Last Edited: 11/11/2024 15:53
"""

def duplicate_integer(nums: list[int]) -> bool:
    """
    Check if an arrar contains duplicate integers.

    Examples:
        >>> input1 = [1, 2, 3, 3]
        >>> input2 = [1, 2, 3, 4]
        >>> duplicate_integer(input1)
        True
        >>> duplicate_integer(input2)
        False
    """

    harshset = set()
    for n in nums:
        if n in harshset:
            return True
        harshset.add(n)
    return False



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
