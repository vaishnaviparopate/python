# def cal_sum(a,b):
#     return a+b
# sum=cal_sum(1,2)
# print(sum)

# waf to rpint length of list.
# cities=["delhi","mumbai","amaravti"]
        # n=input()
        # cities=list(map(str,input().split()))
        # def cal_len(list):
        #     print(len(list))
        
        # cal_len(cities)
# print element in on e line,
        # def line(i):
        #     for i in cities:
        #         print(i,end=" ")
        # line(cities)
# write the factorial of n.
# n=int(input())
# def fac_num(val):
#         fac=1
#         for i in range(1,n):
#                 fac=fac*i
#                 print(fac)
# fac_num(n)

# waf to convert USD TO INR
        # usd=int(input())
        # def usd_value(val):
        #     inr=usd*83
        #     print(inr)
        # usd_value(usd)
# waf program even or odd
# n=int(input())
# def evenodd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# evenodd(n)



# a=[7,2,4,2,6,9]
# a.sort(reverse=True)
# print(a)



# for i in range(int(input())):
#     m,n=map(int,input().split())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     sum1=0
#     sum2=0
#     l1=len(a)
#     l2=len(b)
#     while((l1+l2) < 11):
#         for i in (a):
#             p=max(a)
#             sum1=sum1+p
#             p.delete
#         for i in (b):
#             p=max(b)
#             sum2=sum2+p
#             p.delete
#     u=sum1+sum2 
#     if u>100:
#         print("-1")
#     else:
#         print(u)
        


#         Given a list of 
# 𝑁
# N batsmen and 
# 𝑀
# M bowlers, each with a given cricketing skill, the selectors are asked to pick a team of 
# 11
# 11 players such that the team has at least 
# 4
# 4 batsmen and 
# 4
# 4 bowlers.

# Find is the maximum total cricketing skill of a team which they can form.
# Note that the total cricketing skill is the sum of cricketing skills of all the players in the team.

# Print 
# −
# 1
# −1 if making a valid team is not possible.


# a=[5,3,5,2,4,5,3]
# b=[7,5,8,1,3,9,2]
# ans=0
# a.sort(reverse=True)
# b.sort(reverse=True)
# s1=sum(a[:4])
# l=a[4:]+b[4:]
# l.sort(reverse=True)
# ans+=sum(l[:3])
# print(s1)
# print(a)
# print(l)
# print(ans)


conssole