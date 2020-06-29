"""
给定一个包含n个整数的数组nums和一个目标值 target，判断nums中是否存在四个元素 a，b，c和 d，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。
示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
"""


# class Solution:
#     def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
#         n = len(nums)
#         if n < 4:
#             return []
#         ans = []
#         nums.sort()
#         if target >= 0:
#             for i in range(n):
#                 if nums[i] > target:
#                     return ans
#                 if i > 0 and nums[i] == nums[i-1]:
#                     continue
#                 for j in range(i+1, n):
#                     if nums[i] + nums[j] > target:
#                         return ans
#                     if j > i+1 and nums[j] == nums[j-1]:
#                         continue
#                     L = j + 1
#                     R = n -1
#                     while L < R:
#                         add = nums[i] + nums[j] + nums[L] + nums[R]
#                         if add == target:
#                             ans.append([nums[i], nums[j], nums[L], nums[R]])
#                             while L < R and nums[L] == nums[L+1]:
#                                 L += 1
#                             while L < R and nums[R] == nums[R-1]:
#                                 R -= 1
#                             L += 1
#                             R -= 1
#                         elif add < target:
#                             while L < R and nums[L] == nums[L+1]:
#                                 L += 1
#                             L += 1
#                         else:
#                             while L < R and nums[R] == nums[R-1]:
#                                 R -= 1
#                             R -= 1
#         else:
#             for i in range(n-1, 0, -1):
#                 if nums[i] < target:
#                     return ans
#                 if i < n-1 and nums[i] == nums[i+1]:
#                     continue
#                 for j in range(i-1, 0, -1):
#                     if nums[i] + nums[j] < target:
#                         return ans
#                     if j < i-1 and nums[j] == nums[j+1]:
#                         continue
#                     L = 0
#                     R = j - 1
#                     while L < R:
#                         add = nums[i] + nums[j] + nums[L] + nums[R]
#                         if add == target:
#                             ans.append([nums[L], nums[R], nums[j], nums[i]])
#                             while L < R and nums[L] == nums[L+1]:
#                                 L += 1
#                             while L < R and nums[R] == nums[R-1]:
#                                 R -= 1
#                             L += 1
#                             R -= 1
#                         elif add < target:
#                             while L < R and nums[L] == nums[L+1]:
#                                 L += 1
#                             L += 1
#                         else:
#                             while L < R and nums[R] == nums[R-1]:
#                                 R -= 1
#                             R -= 1
#         return ans


# 正解
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        if n < 4:
            return []
        ans = []
        nums.sort()
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + 3*nums[i+1] > target:
                break
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + 2*nums[j+1] > target:
                    break
                L = j + 1
                R = n - 1
                new_target = target - nums[i] - nums[j]
                while L < R:
                    add = nums[L] + nums[R]
                    if add == new_target:
                        ans.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while L < R and nums[R] == nums[R-1]:
                            R -= 1
                        L += 1
                        R -= 1
                    elif add > new_target:
                        while L < R and nums[R] == nums[R-1]:
                            R -= 1
                        R -= 1
                    else:
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        L += 1
        return ans





