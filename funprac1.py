# Write a Python function called reverse_string that takes a string as input and returns the reverse of that string
        # s=input()
        # def rev_str(s):
        #     str1=" "
        #     p=len(s)
        #     for i in range(p):
        #         str1=s[::-1]
        #     print(str1)
        # rev_str(s)

# find max
n=int(input())
m=list(map(int,input().split()))
def max_fun(val):
    p=max(m)
    print(p)
max_fun(m)