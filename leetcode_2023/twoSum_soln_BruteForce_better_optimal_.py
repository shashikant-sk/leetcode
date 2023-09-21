
# # #-------- Brute force solution----------------
# from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
    
# # #-------- Brute force solution----------------

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Create an empty dictionary to store the elements of 'nums' as keys and their indices as values.
#         nums_hash = {}

#         # Iterate over the 'nums' list along with their indices using 'enumerate'.
#         for i, num in enumerate(nums):
#             # Calculate the complement, which is the value that needs to be added to 'num' to achieve the 'target' sum.
#             complement = target - num

#             # Check if the 'complement' is present in the 'nums_hash' dictionary.
#             if complement in nums_hash:
#                 # If the 'complement' is present, it means we have found two numbers whose sum is equal to the 'target'.
#                 # Return the indices of the two numbers as a list.
#                 return [nums_hash[complement], i]

#             # If the 'complement' is not present in the 'nums_hash' dictionary, add the current 'num' as a key,
#             # and its index 'i' as the value to the dictionary.
#             nums_hash[num] = i

#         # If no solution is found during the iteration, return an empty list to indicate that there is no pair
#         # of numbers in the 'nums' list whose sum is equal to the 'target'.
#         return []


# #-------- Better solution----------------

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        nums_hash = {}
#        n= len(nums)
#        for i in range(n):
#            complement = target - nums[i]
#            if complement in nums_hash:
#                return [nums_hash[complement], i]
#            nums_hash[nums[i]] = i
#        return []


# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     num_indices = {}  # Dictionary to store the indices of numbers

    #     for i, num in enumerate(nums):
    #         complement = target - num  # Calculate the complement needed

    #         if complement in num_indices:
    #             return [num_indices[complement], i]  # Found a pair that sums up to the target

    #         num_indices[num] = i  # Store the current number and its index

    #     return []  # Return an empty list if no valid pair is found
