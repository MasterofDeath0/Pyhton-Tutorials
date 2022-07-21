# check if a no. is multiple of 5

# from ast import While


# a=int(input())
# b=int(input())
# print(a%5)

# if a%5==0:
#     s=a
# elif a%5==1:
#     s=a+4
# elif a%5==2:
#     s=a+3
# elif a%5==3:
#     s=a+2
# else:
#     s=a+1
# print(s)

# for i in range(s,b+1,5):
#     print(i)

#----------------------------------------------------------------

# # if a no. is prime or not

# n = int(input())
# flag = False 

# for d in range(2, n, 1):
#     if n%d==0:
#         flag = True

# if flag:
#     print("the no. is not prime")
# else:
#     print("the no. is prime")

#----------------------------------------------------------------

# # Use of Break

# n = int(input())
# flag = False 

# for d in range(2, n, 1):
#     if n%d==0:
#         flag = True
#         print(d)
#         break

# if flag:
#     print("the no. is not prime")
# else:
#     print("the no. is prime")

#----------------------------------------------------------------

# print all the prime no. from 2 to n

# n = int(input())
# # k=2

#### using while loop
# # while k<=n:
# #     d=2
# #     flag = False
# #     while d<k:
# #         if k%d==0:
# #             flag = True 
# #             break
# #         d=d+1
# #     if not flag:
# #         print(k)
# #     k=k+1


#### using For loop
# for k in range(2,n,1):
#     flag = False
#     for d in range(2,k,1):
#         if k%d==0:
#             flag = True 
#             break
#     if not flag:
#         print (k)

#----------------------------------------------------------------

## if a no. is prime or not

# n=int(input())

# for i in range(2,n):
#     if n%i==0:
#         print("non prime")
#         print(i)
#         break
    
# else:
#     print("prime")
        
#----------------------------------------------------------------

## Print the reverse of a no.

# n=int(input("enter a no. \n"))
# temp = n
# rev = 0

# while temp > 0:
#     last=temp%10
#     print(last)
#     temp=temp//10
#     print(temp)
#     rev=rev*10+last
# print(rev)

#----------------------------------------------------------------

## Palindrome Number

# n=int(input())
# temp = n
# rev = 0

# while temp>0:
#     rev = (rev*10)+(temp%10)
#     temp=temp/10
# print(rev)
# if rev==n:
#     print("True")
# else:
#     print("False")

#----------------------------------------------------------------
