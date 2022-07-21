## TUPLES
# Tuples are like Lists but unlike lists they are immutable (can't make changes in it)

# a=1,2
# print(type(a))

## -------------------------------------------------------------------

# Operations on a Tuple

# a=1,2
# b=(3,4)

# c=a+b
# print(c)

# d=a,b
# print(d)

# we can perform all the functions of a lists except append, remove, update

# del(d)
# print(d) # shows error as d is not defined after deletion

## -------------------------------------------------------------------

# Variable length of input and output

# def sum_mul(a,b,*c):   # here *c acting as a tuple where we can store as many no. as possible
#     ans=a+b
#     mul=a*b
#     for i in c:
#         ans+=i
#         mul*=i
#     return ans,mul

# ans2 = sum_mul(1,2,3,4,5,6,7,8,9)   # here ans2 is acting as tuple to give out variable outut as func sum_mul is returning more than one value
# print(ans2)

## -------------------------------------------------------------------

## DICTIONARIES
# they are used to use any no. or string as a key or a value unlike lists or tuples in which we can only use index as a key to find objects

# a={"the":1, "a":3, "an":5, 10000:"articles"}
# print(type(a))
# print(a)
# print(len(a))

# b=a.copy()
# print(b)

# c=dict([("the",1),("a",10),(2,3)]) #typecasting

# d=dict.fromkeys(["abc",32,"sanyam",64,34])
# print(d) # this will print None as a value for all three keys
# d=dict.fromkeys(["abc",32,"sanyam",64,34],10)
# print(d) # this will print 10 as a value for all three keys

## -------------------------------------------------------------------

## DICTIONARIES FUNCTIONS

# a={"the":1, "a":3, "an":5, 10000:"articles"}
# a["the"]=10
# print(a)   #updating type 1

# a={"the":1, "a":3, "an":5, 10000:"articles"}
# b={"sanyam":"he","a":5,"the":1,1400:4}
# a.update(b)    #updating type 2
# print(a)

# a.pop("sanyam")    #popping out a single element 
# print(a)
# del a["a"]    #deleting a single element
# print(a)
# a.clear()   #clearing out whole dict 
# print(a)
# del a  #deleting whole dict 
# print(a)

## -------------------------------------------------------------------

## Print all words with frequency K

# def kfreqwords(s,k):
#     words=s.split()
#     d={}
#     for w in words:
#         d[w]=d.get(w,0)+1
#     for w in d:
#         if d[w]==k:
#             print(w)

# str=input()
# k=int(input())
# word_freq=kfreqwords(str,k)

## -------------------------------------------------------------------

## SETS
# they are basically a mathematical set and dictionary without any key:value pair

# a={"sanyam","aggarwal","books",24,36,67}
# print(type(a))

# print("sanyam" in a)   #to check whether the particular word/no. is present in a set or not

# a={"sanyam","aggarwal","books",24,36,67}
# for s in a:
#     print(s)   #to print elements

# a={"sanyam","aggarwal","books",24,36,67}
# a.add("college")  #adding elements in a lists
# print(a)

# a={"sanyam","aggarwal","books",24,36,67}
# b={"macbook","apple",64,24,36,78}    #adding/updating lists
# a.update(b)
# print(a) 

# a.remove("sanyam")   #removes the element
# print(a)
# a.discard(64)  #elements present in set gets discarded 
# a.discard(23)  #element not present in set when discarded does not show any error
# print(a)
# a.pop()   #popping our a single element
# print(a)


a={1,2,3,4}
b={3,4,5,6}
d={1,2,3,4,6,5,7,8,9}
c={9,87,0}

# print(a.intersection(b))
# print(a.union(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))
# (a.intersection_update(b))
# print(a)
# print(a.union_update(b))    #no such function
# (a.difference_update(b))
# print(a)
# (b.difference_update(a))
# print(b)
# (a.symmetric_difference_update(b))
# print(a)

print(a.issubset(d))
print(d.issuperset(a))
print(a.isdisjoint(c))






