"""method.py: writting and using methods"""

# keywords: def, return, pass
# syntax:
#
# def method_name([params]):
#     pass
#

a = 100
b = 200
c = 300
#above variables are global and are accessible all from the entire module.

def adder(a,b):
    """adds two numbers, strings or iterables"""
    #a, b are local to this method.
    # they cannot be accessed outside this method.
    #global c
    c = 10
    return (a+b+c, a, b)

print(adder(10,20))
print("global c:"+str(c))


def multiplier(a,b):
    if a>b:
        return a
    return a*b

def demo_method(a,b,c, call_type="", call_for=""):
    print(a+b+c)


demo_method('a','b','c')

demo_method( a='a', c='c', b='b')


#variable arguments

def var_args_method(a,b, *args, **kwargs):
    print("a :" + str(a) )
    print("b : %s" % (b,))
    for arg in args:
        print("var arg: %s" % arg)

    for key, kwarg in list(kwargs.items()):
        print("%s : %s" % (key, kwarg))

var_args_method('a','b')
var_args_method("a", 10, 12,3,4,5, name="John", age=23, country="USA")


print("a: {}, b: {}, c : {}".format(a,b,c))

print("a: {1}, b : {0}, c : {2} ".format(b,a,c))

print("a: {a}, b:{b}, c:{c}".format(a=a, b="hello", c=c))
