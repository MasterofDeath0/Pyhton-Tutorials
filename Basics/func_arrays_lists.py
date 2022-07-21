### LISTS 

# li=[1,2,3,"Sanyam",4,5,6,"Aggarwal"]
# print(li[5])

#----------------------------------------------------------------

## Operations on lists

## Modification

# li=[1,2,3,4,5,"Sanyam","Ayushi",3.4,5.4]
# print(li)
# print(li[5])
# print(li[7])
# li[7]=9
# print(li)

#----------------------------------------------------------------

## Insertion

# li=[1,2,3,4,5,"Sanyam","Ayushi",3.4,5.4]
# li.append(10)
# #print(li)
# li.insert(16,"MasterofDeath")
# #print(li)
# li.append([1,2,3,4]) ## adds list in a list
# #print(li)
# li.extend([1,2,3,4]) ## adda as an element
# #print(li)

# #----------------------------------------------------------------

# ## Deletion

# li=[1,2,3,4,5,"Sanyam","Ayushi",3.4,5.4]
# print(li)
# li.pop()  ## removes element from last
# print(len(li))
# print(li)
# li.pop(3) ## removes element from that index
# print(len(li))
# print(li)
# li.remove(2) ## removes that element whuch is mentioned in parenthesis 
# print(li)
# print(len(li))

#----------------------------------------------------------------

## Looping On Lists

# li=[1,2,3,4,5,"Sanyam","Ayushi",3.4,5.4]

## Way 1
# for i in range (len(li)):
#     print(li[i])
## Way 2
#for i in range (3,len(li)):
#    print(li[i])
## Way 3
# for ele in li:
#     print(ele)
## Way 4
#for ele in li[2:8:2]:
#    print(ele)

#----------------------------------------------------------------

## Negative Indexing 

# li=[1,2,3,4,5,"Sanyam","Ayushi",3.4,5.4]
# print(li[-1])
# print(li[-2])
# print(li[-3])
# print(li[-4])
# print(li[-5])
# print(li[-10]) ## index out of range

#----------------------------------------------------------------

## Slicing

li=[1,2,3,4,5,"Sanyam","Ayushi",3.4,5.4]
print(li[:-1])

#----------------------------------------------------------------

## Taking Inputs

# Line Separated Inputs 
# n=int(input())
# li=[]
# for i in range(n):
#     a=int(input())
#     li.append(a)
#print(li)

#----------------------------------------------------------------

## Space Separated inputs

# str=input()
# print(str)
# str1=str.split(',')
# print(str1)
# li = []
# for ele in str1:
#     li.append(int(ele))
# print(li)


## Space separated inputs in one step  

# li = [int(x) for x in input().split()]
# print(li)

#----------------------------------------------------------------

## Linear Search
# def Linear_Search(li,n):
#     for i in range(len(li)):
#         if li[i]==n:
#             return i
#     return -1

# li=[1,2,3,4]
# n=input()
# ans=Linear_Search(li,n)
# print(ans)

#----------------------------------------------------------------

## Reverse Lists
# def reverse(li):
#     length=len(li)
#     for i in range (length//2):
#         li[i],li[-i-1]=li[-i-1],li[i]

# li=[1,2,3,4,5,6,7]
# reverse(li)
# print(li)




### FUNCTIONS

## Factorial Function

# def fac(a):
#     fact=1
#     if (a==0):
#         return fact
#     else:
#         for i in range(1,a+1):
#             fact=fact*i
#     return fact        

# n=int(input())
# print(fac(n))

