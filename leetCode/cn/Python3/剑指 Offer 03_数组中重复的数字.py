# @algorithm @lc id=100275 lang=python3
# @title shu-zu-zhong-zhong-fu-de-shu-zi-lcof


from cn.Python3.mod.preImport import *

# @test([2, 3, 1, 0, 2, 5, 3])=2
# @test([2, 3, 1, 0, 3, 5, 1])=1
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]