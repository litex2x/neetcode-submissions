class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in hash and not i == hash[diff]:
                return [i, hash[diff]]