# Solution for leetcode 0001 Two Sum
# Idea: sort the list then start from the begining and the end
# Time complexity:  O(len(nums))
# Space complexity: O(len(nums))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = sorted(nums)
        i,j = 0,len(nums)-1
        while l[i]+l[j]!=target:
            if l[i]+l[j]<target:
                i+=1
            else:
                j-=1

        if l[i]==l[j]:
            i = nums.index(l[i])
            return [i,nums[i+1:].index(l[j])+i+1]
        return sorted([nums.index(l[i]),nums.index(l[j])])

