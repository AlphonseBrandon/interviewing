"""
Author: Alphonse Brandon
Date Created: 12/11/2024 15:00
Last Edited: 12/11/2024 15:30
"""

# Sorting Solution

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
        return false

    return sorted(s) == sorted(t)
    
    


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
