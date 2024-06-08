# leap year
        # n=int(input())
        # if (n%4==0 and n%100!=0) or n%400==0:
        #     print("yes")
        # else:
        #     print("not")

# n=int(input())
# def leap_num(n):
#     if (n%4==0 and n%100!=0) or n%400==0:
#         print("yes")
#     else:
#         print("not")
# leap_num(n);      

# Create an if-elif-else block to determine the grade based on a student’s score (e.g., A for 90-100, B for 80-89, etc.).
# n=int(input())
# def student(n):
#     if n>=90 and n<100:        
#         print("A")
#     elif n>=80 and n<89:
#         print("B")
#     else:
#         print("invalid")
# student(n)

# Generate the first n prime numbers using a while loop.
# n=int(input())
# def prime_num(n):
#     c=1
#     i=1
#     while c<=n:
#         c1=0
        
#         for j in range(1,i+1):
#             if i%j==0:
#                 c1=c1+1
#                 # j=j+1
#         if c1==2:
#             print(i)
#             c=c+1
#         i=i+1
# prime_num(n)


# Calculate the sum of all even numbers from 1 to 100 using a for loop.
# n=int(input())
# def even_sum(n):
#     sum=0
#     for i in range(1,n+1):
#         if i%2==0:
#             sum=sum+i
#     print(sum)
# even_sum(10)

# Write a Python function that takes a list of integers as input and returns the product of all positive numbers in the list.
# n=int(input())
# arr=list(map(int,input().split()))
# def product(n):
#     p=1
#     for i in range(n):
#         p=p*arr[i]
#     print(p)
# product(n)

# Create a list of fruits and print each fruit in reverse order.

# s = int(input())
# string = list(map(str,input().split()))  # corrected from input.split() to input().split()

# def rev(string):
#     p = " "
#     for i in string:
#         p = p + i[::-1]  # corrected from i[::1] to i[::-1]
#     print(p,end=" ")

# rev(string)  # corrected from rev(s) to rev(string)



# fruits = input("Enter the fruits separated by spaces: ").split()

# # Iterate through each fruit and print it in reverse order
# for fruit in fruits:
#     print(fruit[::-1])

# Define a tuple containing the names of three programming languages. Print each language name along with its length.
# name=input().split()
# for i in name:
#     p=len(i)
#     print(i,"len=",p)

# Create a Python function that checks if two sets are disjoint (i.e., have no common elements)
# n=input("enter the number:")
# s=input().split()
# s2=input().split()
# usr=set(s)
# usr1=set(s2)
# mer=usr|usr1
# print(mer)

# n=int(input("enter the number:"))
# s=input().split()
# s2=input().split()
# usr=set(s)
# usr1=set(s2)
# if usr.isdisjoint(usr1):
#     print ("True")
# else:
#     print("False") 

# Find the union of two sets containing integers from 1 to 10 and 5 to 15.
# def union_set(s,s2):
#         usr=set(s)
#         usr1=set(s2)
#         # l=s|s2
#         return usr|usr1

# n=int(input())
# s=list(map(int,input().split()))
# s2=list(map(int,input().split()))
# result=union_set(s,s2)
# print(result)

# Create a dictionary representing a book with keys for title, author, and publication year.
# s=list(map(str,input().split()))
# s2=list(map(int,input().split()))
# def key_value(v,v2):
#     result=dict(zip(v,v2))
#     print(result)
# key_value(s,s2)

# Write a function that takes a list of numbers and returns the maximum value.
# n=int(input())
# l=list(map(int,input().split()))
# p=max(l)
# print(p)

# Create a Python program that reads an integer from the user. Handle any invalid input (e.g., non-integer values) by displaying an appropriate error message.
# n=input()
# try:
#     user=int(n)
#     print("you enterd:",n)
# except ValueError:
#     print("error:")

# Raise a custom exception when dividing by zero in a function.


# def custom(val1,val2):
#       if (val2==0):
#             return "Error"
#       else:
#             return val1/val2
# val1=int(input())
# val2=int(input())
# print(custom(val1,val2))

# Write a Python function that takes two sets as input and returns their intersection (common elements).
# s=list(map(int,input().split()))
# s2=list(map(int,input().split()))
# v1=set(s)
# v2=set(s2)
# def intser(v1,v2):
#     v1=set(s)
#     v2=set(s2)

#     p=v1.intersection(v2)
#     print(p) 
# intser(s,s2)    


# n=int(input())
# b=bin(n)[2:]
# l=len(b)
# s=0
# for i in range(l):
#         if b[i]=="1":
#                 s=s+1
# print(s)

# Initialize a list to store the integers
integers = []

# Take input until a 0 is encountered
while True:
    num = int(input())
    if num == 0:
        break
    integers.append(num)

# Print the integers in reverse order
for num in reversed(integers):
    print(num)




