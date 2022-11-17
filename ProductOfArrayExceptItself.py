# AMAZON INTERVIEW QUESTION

class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

		# product of all numbers before i
        left_product = 1
        for i in range(len(nums)):
			# let answer[i] = product of numbers left of i
            answer[i] = left_product
			# update left_product to include i for the next iteration (i+1)
            left_product *= nums[i]

		# product of all numbers after i
        right_product = 1
        for i in reversed(range(len(nums))):
			# now answer[i] = left_product * right_product for all i
            answer[i] *= right_product
            # update right_product to include i for next iteration (i-1)
            right_product *= nums[i]
            
        return answer