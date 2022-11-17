class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_hashmap={}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_hashmap:
                return [prev_hashmap[diff], i]
            prev_hashmap[n] = i
        return

## use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice;
## We iterate through the array and calculate if the { target  - current value } is already in the hashmap
## If it's already in the hashmap, we return the indices and solution is complete.
## Time complexity at worst is 0(n)
