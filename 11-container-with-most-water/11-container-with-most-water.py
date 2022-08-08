class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_area=0
        j=n-1
        i=0
        while i<j:
            length=min(height[i],height[j])
            width=j-i
            area=length*width
            max_area=max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
                
        return max_area
        