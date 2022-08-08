class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        if n>=k:
            sums=sum(nums[0:k])
            curr=sums/k
            j=0
            for i in range(k,n):
                sums+=nums[i]
                sums-=nums[j]
                j+=1
                curr=max(sums/k,curr)
        else:
            return sum(nums)/n
        return curr
        