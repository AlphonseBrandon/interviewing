"""
Author: Alphonse Brandon
Date Created: 12/11/2024 15:00
Last Edited: 12/11/2024 15:30
"""



def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams.

    Example 1:
        >>> is_anagram(s="racecar", t="carrace")
        True

    Example 2:
        >>> is_anagram(s="jar", t="jam")
        False
    """
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
