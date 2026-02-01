class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        l1=[]

        for _ in range(26):
          l1.append(0)

        for index in range (len(s)):
            l1[ord(s[index])-97] +=1      
            l1[ord(t[index])-97] -=1 
        for v in l1:
            if(v!=0):
                return False
        return True        
obj=Solution()
print(obj.isAnagram("hello","llohe"))