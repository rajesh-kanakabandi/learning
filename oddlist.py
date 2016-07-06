"""
	oddList.py
"""

def oddList(l1):
	return l1[1::2]

def odd_list(l1):
	return [l1[i] for i in range(len(l1)) if i % 2 != 0]

print(oddList([0,1,2,3,4,5,6]))
print(odd_list([0,1,2,3,4,5,6]))

assert(oddList([0,1,2,3,4,5,6])==[1,3,5])

def cum_sum(l1):
	cum = 0
	result = []
	for item in l1:
		cum = cum + item
		result.append(cum)
	return result

print(cum_sum([1,1,1]))