"""
    Control Flows: if, else, elif
"""

i = -10

if i==0:
    print("Zero")
elif i > 0:
    print("Positive")
else:
    print("Negative")

i = 10
while i>0:
    print(i)
    i= i-1
else:
    print("loop terminated")

for i in range(10,0,-1): # 10 in [10,9,8,7..1]
    print(i)
else:
    print("For loop terminated")


list1 = [123,32,45]
dict1 = {'name': 'john', 'age': 23, 'country':'USA'}

for item in list1:

    print(item)

for item in dict1.keys():
    print(item)
    print(dict1[item])

for value in dict1.values():
    print(value)
import pdb; pdb.set_trace()
for item_key, item_val in list(dict1.items()):
    print(item_key + " : " + str(item_val))


for i in range(10,0,-1):
    if i % 2 ==0:
        continue
    # if i == 1:
    #     break
    print(i)
else:
    print("For loop terminated")


if something:
    #implement after so and so
    pass
