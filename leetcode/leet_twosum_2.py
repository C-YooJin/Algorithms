class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        i = 0
        for num in nums:
            if target - num in dic:
                return dic[target-num], i
            dic[num] = i
            i += 1
