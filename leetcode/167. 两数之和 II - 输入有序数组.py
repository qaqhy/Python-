"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            if numbers[L] + numbers[R] < target:
                L += 1
            elif numbers[L] + numbers[R] > target:
                R -= 1
            else:
                return [L+1, R+1]