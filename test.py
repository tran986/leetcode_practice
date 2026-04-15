# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
class Solution(object):
    def twoSum(self, nums, target):
        #:type nums: List[int]
        #:type target: int
        #:rtype: List[int]
        nums = input("type nums: ")
        target = input("type target: ")
s = Solution()
print(s.twoSum(4,2))
"""
      
nums = [2,7,11]
target = 9

id=1
for i in range(len(nums)):
    n=nums[i] 
    id = id + 1
    print(n + nums[id])
    #print(f"idx {i} - {n}")
    
        
