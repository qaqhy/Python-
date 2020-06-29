"""给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c，使得a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。 注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ns = []
        for i in range(n):
            if nums[i] > 0:
                return ns
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                add = nums[i] + nums[L] + nums[R]
                if add == 0:
                    ns.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif add < 0:
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    L += 1
                else:
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    R -= 1
        return ns
