def large_pal(digits):
    max_num = int('9'*digits)
    min_num = int('9' * (digits-1) ) + 1
    max_pal = 0
    adder(1,2)
    for i in range(max_num, min_num, -1):
        for j in range(max_num, min_num, -1):
            prod = str(i*j)
            if prod == prod[::-1]:
                if max_pal < int(prod):
                    max_pal = int(prod)
                    max_i = i
    print("{} = {} * {}".format(max_pal, max_i, int(max_pal/max_i)))


def small_pall():
    pass

def adder(a,b):
    pass

if __name__ == '__main__':
    #all initialization steps
    large_pal(3)

#__doc__,
#
# 999 * 999 = xyz str(xyz) == str(xyz)[::-1]
# 999 * 998
# ...
# 999 * 100 990099
#
# 998 * 998
# 998 * 997 9901099
# 998 * 996
# ...
# 998 * 100
#
#

#form and import

#from tells which module to import from.

#import can imprt a module, class, method, variable

#from copy import deepcopy

# import copy
#
# copy.deepcopy()
