#range
"""
list = [1,2,3]

for item in range(50,100,20): # range ile 50'den basla 100 ' e kadar , 20 aralklarla diye liste olusturduk
    print(item)

    print(list(range(50,100,10))) # list'e aktardık 


  """  

# enumerate

"""
index = 0
greeting = 'Hello There'

for index,letter in enumerate(greeting) : #key,value olusturduk
    print(f"index: {index} letter : {letter}")
    index += 1
"""

# zip 

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)