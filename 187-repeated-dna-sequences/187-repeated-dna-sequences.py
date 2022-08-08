class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mini=[]
        dict={}
        n=len(s)
        for i in range(0,n-9):
            if (s[i:i+10]) not in dict:
                dict[s[i:i+10]]=1
            else:
                if dict[s[i:i+10]]==1:
                    mini.append(s[i:i+10])
                    dict[s[i:i+10]]+=1
        return mini