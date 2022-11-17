class Solution(object):
    def containsDuplicate(self, nums):
        # EASY QUESTION
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Put everything we iterate in a set
        # If the current value is in the set, return True
        # If the asked value never appears in the set, Return False.
        hashset = set()
        # Loop through the list
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False