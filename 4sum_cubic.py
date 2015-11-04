class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length<4:
            return []
        list.sort(nums)
        result = []
        for x in range(length-3):
            if x>0 and nums[x]==nums[x-1]:
                continue
            for y in range(x+1,length-2):
                if y>x+1 and nums[y]==nums[y-1]:
                    continue
                i = y+1
                j = length-1
                while i<j:
                    if nums[i]+nums[j]<target-nums[x]-nums[y]:
                        i+=1
                    elif nums[i]+nums[j]>target-nums[x]-nums[y]:  
                        j-=1
                    else:
                        while i+1<j and nums[i]==nums[i+1]:
                            i+=1
                        while i<j-1 and nums[j]==nums[j-1]:    
                            j-=1
                        result.append([nums[x],nums[y],nums[i],nums[j]])
                        i+=1
                        j-=1
        return result
