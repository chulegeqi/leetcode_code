# link of the code
# https://leetcode.com/problems/combination-sum-ii/

# The problem is actually search in the form of dfs. IF violates the constraint, then pop the most recent 
# element, try out new element.

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #[1,1,2,5,6,7]
        if not candidates:
            return []
        candidates.sort()
        results = []
        def sum_helper(start, path, end, target):
            if target == 0:
                #print(path)
                # if use results.append(path), path will be modified during the execution
                # create a copy of path using path[:]
                results.append(path[:])
            if target < 0 or start > end:
                return a
            for i in range(start, end+1):
                if i-1 >= start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                #print(path)
                sum_helper(i+1,path,end,target-candidates[i])
                path.pop()
        sum_helper(0,[],len(candidates)-1,target)
        return results
