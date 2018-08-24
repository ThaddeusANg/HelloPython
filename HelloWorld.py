print("Just learning python please ignore")
print("Lesson 1")
print("Hello World")
x = 1
if x == 1:
    print("x is 1")

print("Goodbye World")
print("")

print("Lesson 2 variables")
test = "test"
print(test+" is a string")

floatingNum = 12.34
print(floatingNum, "is a floating num")

num = 1
print(float(num), "is cast to a floating num")

a,b = 3,4
print(a,b, "are declared simultaneously and if separated by comma are treated as strings")

sample = 15.5
if isinstance(sample, float):
    print(sample, "is of floating number type")
    print("check instancetypes with isinstance(variable, type)")

print("")

print("Lesson 3")
myList = [];
myList.append(1);
myList.append(2);
myList.append(3)
print(myList, "this is a list of 3 elements")
print(myList[0], "access cells by index as normal")
print(len(myList), "elements")
print("len(object)")
print("Notes: wrapper around object.__len__(self")
print("")
print("right way to test for null lists")
if myList:
    print("myList has Items")
    print("syntax: if myList")
    print("using len(myList) is inefficient")

emptyList = []
if emptyList:
    print("emptyList has no items")
    print("just testing 'if emptyList'")

print("")
stringInterpolation = "String Interpolation"
reaction = "yay!"
print(f"{stringInterpolation}! {reaction}")
print('syntax is print(f"{variable name}")')

print("")
print("Lesson 4")
mod = 11%3
print("11 % 3", mod)
print("syntax: basic modulo operator %")

print("")
print("2**2 => ", 2**2)
print("2**3 => ", 2**3)
print("syntax: ** creates a power relation ship, base ** exponent")

print("")
print("This" + " " + "basic" + " " + "String" + " " + "concatenation")

print("")
print("badger " * 5)
print("syntax: ('string' * count) creates a repeating sequence")

print("")
print("[1,2,3] + [2,4,6] =>", [1,3,5]+[2,4,6])
print("syntax: adding two lists together blends them, no need for AddRange methods")

print("")
x = "x object"
y = "y object"

x_list = [x]*10
y_list = [y]*10
xAndY = x_list+y_list

print("syntax notes: for duplicating elements in the same list ([list] * xTimes)")
print(x_list)
print(f"x_list has {len(x_list)}")
print(f"y_list has {len(y_list)}")
print(f"xAndY has {len(xAndY)}")

print("")
if x_list.count(x) == 10:
    print(f"x_list has {x_list.count(x)} x objects")
    print("syntax notes: the .count x must be exactly the object contained, x != [x]")

print("")
if xAndY.count(x) == 10 and xAndY.count(y) == 10:
    print("syntax notes: multiple boolean statements use and not &&")
    print(f"xAndY has {xAndY.count(x)} x's and {xAndY.count(y)} y's")
