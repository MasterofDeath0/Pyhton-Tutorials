# str="My Name Is Sanyam Aggarwal"
# print(str)
# str='I Live in Delhi'
# print(str)
# str="""I   
# Am 
# MasterofDeath0"""   ##multiline strings
# print(str)

## -------------------------------------------------------------------

## Strings Are Immutable (you can't ammend it)

# str="My Name Is Sanyam Aggarwal"
# print(str)
# str[0]="A"  
# print(str)

## -------------------------------------------------------------------

# str1="My Name Is Sanyam Aggarwal"
# str2="My Name Is Sanyam Aggarwal"
# if id(str1)==id(str2):
#     print("they are same")
# else:
#     print('they are not same')

## -------------------------------------------------------------------

## Concatenation of Strings

# str="My Name Is Sanyam Aggarwal"
# str1=str + " I live in Delhi"
# print(str1)

# str1 = 'horcrux'
# str2 = str1 + str(6)
# print(str2)

## -------------------------------------------------------------------

## Slicing of Strings

## It is same as that in Lists, no change

## -------------------------------------------------------------------

## Iterating on Strings

# str="my name is Sanyam Aggarwal"
# count=0
# for i in range(len(str)):
#     if (str[i]=='a'):
#         count = count+1
# print(count)

# for letter in str:
#     if (letter == "a"):
#         count=count+1
# print(count)

## IN and NOT IN operations

# substr = input()
# if substr in str:
#     print("yes")
# else:
#     print("no")

# substr = input()
# if substr not in str:
#     print("yes")
# else:
#     print("no")

## -------------------------------------------------------------------

## Operations on Strings

## Split
# a="my name is MasterofDeath0"
# a=a.split(' ',2)    -------------->       ##splits any string, 2 indicates how many words need to be splitted
# print(a)

## Replace
# a="my name is MasterofDeath0 MasterofDeath0 MasterofDeath0 MasterofDeath0"
# a=a.replace("MasterofDeath0","Sanyam",2)  ----->  ##replaces with any value , 2 indicates how many values need to be changed
# print(a)

## Find
# a="my name is MasterofDeath0"
# index=a.find("Master")        ----------->         ##finds the index of any sub string
# print(index)

## Lower and Upper 
# a="My Name is masterofdeath0"
# a=a.lower()
# print(a)
# a=a.upper()
# print(a)

## Starts With
# a="My Name is masterofdeath0"
# ans=a.startswith("My Nae")
# print(ans)

## -------------------------------------------------------------------

## Replace with other characters

# def replace(str,char1,char2):
#     str1=""
#     for letter in str:
#         if (letter==char1):
#             str1+=char2
#         else:
#             str1+=letter
#     return str1

# str="abcadeafga"
# str=replace(str,'a','e')
# print(str)

## -------------------------------------------------------------------

## Counting vowels, consonants, digits, special characters

# def count(str):
#     v,c,d,s=0,0,0,0
#     for char in str:
#         if ((char>='a' and char<='z')or(char>='A' and char<='Z')):
#             char = char.upper()
#             if (char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
#                 v+=1
#             else:
#                 c+=1
#         elif (char>='0' and char<='9'):
#             d+=1
#         else:
#             s+=1
#     return v,c,d,s


# str="aEIouBCDEFGH12345!@#$"
# v,c,d,s=count(str)
# print(v,c,d,s)

## -------------------------------------------------------------------

## 2D lists

# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(li)

## -------------------------------------------------------------------


## inserting elements in 2D lists
# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# li.insert(2,[1,2,3,8,9])
# print(li)

## -------------------------------------------------------------------

## changing elements in a 2D list

# print(li[0][3])
# li[0][3] = 20
# print(li[0][3])
# print(li)


## -------------------------------------------------------------------

## Storing of 2D lists

# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(li)
# print(id(li))
# print(id(li[0]))
# print(id(li[1]))

## -------------------------------------------------------------------

## Jagged Lists

## column size is not same
# li = [[1,2,3,4],[7,8,9],[11,23]]
# print(li[0])

## -------------------------------------------------------------------

## List Comprehension

# squaring/cubing.....

# li = [1,2,3,4,5]
# li_sq = [n**2 for n in li] --------------> method 1
# for ele in li:
#     li_sq.append(ele**2) --------------> method 2
# print(li_sq)


# li_sq = [n**2   for n in li  ........ ]
        # output   for loop    conditional
# there can be as many conditionals as you want


## -------------------------------------------------------------------

## Input of 2D list

# Type 1 (input each no. separately)
# str=input().split()
# n,m=int(str[0]),int(str[1])
# mat=[]
# for i in range(n):
#   li=[]
#   for j in range(m):
#     li.append(int(input()))
# #   print(li)
#   mat.append(li)
# #   print(mat)
# print(mat)

# Type 2 -----> can be used for jagged list as well (input in one line)
# str=input().split()
# n,m=int(str[0]),int(str[1])
# li = [[int(j) for j in input().split()] for i in range (n)]
# m is not getting used here

# Type 3 (all Input in one line)
# str=input().split()
# n,m=int(str[0]),int(str[1])
# b=input().split()
# li=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
# print(li)

# Type 4 (every Input in one line)
# str=input().split()
# n,m=int(str[0]),int(str[1])
# b=str[2:]
# print(b)
# li=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
# print(li)

## -------------------------------------------------------------------

## Printing of 2D list

# Type 1 (using n & m)
# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(li)
# n=len(li)
# m=len(li[0])
# print(n,m)
# for i in range(n):
#         for j in range(m):
#                 print(li[i][j], end=" ")
#         print()


# Type 2 (can be used for jagged list)
# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(li)
# for i in li:
#         for j in i :
#                 print(j , end=" ")
#         print()


# Type 3 (using join function)
# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(li)
# for i in li:
#         output=" ".join(str(j) for j in i)
#         print(output)


## -------------------------------------------------------------------

## Largest col sum
# def max_col_sum(li):
#         max_sum=-1
#         col_index=-1
#         n=len(li)
#         m=len(li[0])

#         for j in range (m):
#                 sum=0
#                 for i in range (n):
#                 # for ele in li:
#                         sum+=li[i][j]
#                         # sum+=ele(j)
#                 if sum>max_sum:
#                         max_sum=sum
#                         col_index=j
#         return max_sum,col_index

# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,1]]
# lar_sum,lar_col_index=max_col_sum(li)
# print(lar_sum,lar_col_index)
