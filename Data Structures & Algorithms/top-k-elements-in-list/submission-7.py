class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        numLen = len(nums)
        counts = {}
        freq = [[] for i in range(numLen + 1)]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key in counts:
            freq[counts[key]].append(key)
        result = []
        while numLen > 0 and len(result) != k:
            result.extend(freq[numLen])
            numLen -= 1
        return result[0:k]
