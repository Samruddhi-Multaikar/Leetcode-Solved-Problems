class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        people=sorted(people)
        heavy=len(people)-1
        light=0
        while( heavy>=light):
            
            if people[light]+people[heavy]<=limit:
                count+=1
                heavy-=1
                light+=1
            else:
                count+=1
                heavy-=1
                
        return count
        