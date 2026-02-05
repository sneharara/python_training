#using suffix prefix approach
nums=[1,2,3,4]
n=len(nums)
p=1
s=1
answer=[1]*n

#prefix condition
for i in range(1,len(nums)):
    answer[i]=p
    p[i]=p[i-1]*nums[i-1]

#suffix condition
for j in range(len(nums)-2,-1,-1):
    answer[i]*=s
    s[j]=s[j+1]*nums[j+1]

#multiply suffix prefix table
print(answer)