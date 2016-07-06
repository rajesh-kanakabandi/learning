"""
	data_structures.py
	covers data structures in python.
"""

#Lists
	#Declaration

#python debugger: commands - n(next), s(step in), c(continue)
list1 = []
list2 = [1,2,3]
list3 = ["hello", "asdf"]
list4 = ["hell0", 1, 1.5]

#indexes in python start from 0
	#manipulation
list1.append(123) #inserts at the end


list2[2] = 5 #change
list4[1] = 321
import pdb; pdb.set_trace()
list2.remove(2) #rmoves the element 2

#sort():
	#inplace sorting- changes the original list
	#optional parameter: reverse : True/False
#sorted():
	#returns a copy of the sorted list.
	#does not effect the original list.
	#optional parameter: reverse : True/False
	#optional parameter: key: key to sort on.



#print(list1, list2, list3, list4)

#   https://docs.python.org/3/tutorial/datastructures.html?highlight=list
#	http://www.dotnetperls.com/slice-python

# (Pdb) list7 = [0,1,2,3,4,5,6,7,8,9]
# (Pdb) list7[::2]
# [0, 2, 4, 6, 8]
# (Pdb) list7[:2]
# [0, 1]
# (Pdb) list7[-1]
# 9
# (Pdb) list7[:-1]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# (Pdb) list7[-1:]
# [9]
# (Pdb) list7[::-1]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#slicing:

# listObj[startIndex:endIndex:skipElements]
#


for item in list4:
	print (item)


#sets:
	#https://docs.python.org/3/tutorial/datastructures.html?highlight=list#sets


#dictinaries:

#commonly refered as dict

import pdb; pdb.set_trace()
dict1 = {}
dict2 = {'key' : 'value'}
dict2['name'] = 'John'
print(dict2['name'])
dict2['name']
dict2.get('name')
dict2.get('nasdf', "Does not exist")


for key in dict2.keys():
	print(key + " : " + dict2[key])


# https://projecteuler.net/archives
#solve these problems.


print ("***************************Dict Operations************")
dict1= {'name':'Ishan','age':25,'isadult':'yes'}
dict2= {'name':'Anish','age':20,'isadult':'yes'}
dict3 = {'name':'Anish','age':20,'isadult':'yes'}
dict1['age']=23
print (dict1)
print (dict2)

print ("dict equal:", cdict3==dict2)
