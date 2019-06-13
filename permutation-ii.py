# https://leetcode.com/problems/permutations-ii/
# The algorithm is to limit the permutation choice, order is you have to visit i-1 first if nums[i] == nums[i-1] 
# then same element will only have one visiting order

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        size = len(nums)
        results = []
        visited = [False] * size
        def permute_h(path):
            if len(path) == size:
                results.append(path[:])
                return
            for i in range(size):
                if visited[i] or (nums[i] == nums[i-1] and i > 0 and not visited[i-1]):
                    continue
                visited[i] = True
                path.append(nums[i])
                permute_h(path)
                path.pop()
                visited[i] = False
        permute_h([])
        return results
