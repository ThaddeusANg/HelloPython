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

print("")
print("Lesson 5 string formatting")

print("Hello %s" %"world")
print("syntax: 'Hello %s' %var")

print("")
print("To %s multiples, use multiple percent symbols, in this case, %d times" %("use", 2))

print("")
list = [1,2,3]
print("string representation of a list => %s" % list)

print("")
stringInterpolation = "String Interpolation"
reaction = "yay!"
print(f"{stringInterpolation}! {reaction}")
print('syntax is print(f"{variable name}")')

print("")
print("Lesson 6 string operations")
numChain = "1234566777"
print(f"length of numChain is {len(numChain)}")
print("syntax is len(object)")

print("")
print(f"3 is at index {numChain.index('3')} in %s" %numChain)
print("syntax: indexOf is numChain.index('search value')")

print("")
print(f"there are {numChain.count('6')} 6's and {numChain.count('7')} 7's")
print("syntax: to get instances of a value in a string, use .count('value')")

print("")
print(f"slice the string {numChain} from index 3 to index 6 => {numChain[3:6]}")
print("syntax: subString, treat the string like an array, [start index:end index]")
print("syntax: charAt, [index] => returns the character at this index => ")
print("example numChain[3] => " + numChain[3])
print("")
print("syntax: substring before, [:end index] gets the substring from beginning to index")
print("example numChain[:6] => " + numChain[:6])
print("")
print("syntax: substring after, [start index:] gets the substring from index to end")
print("example numChain[3:]=> " + numChain[3:])
print("")
print("syntax: negative index values start at the end of the string")
print("example numChain[-2:] retuns last two elements of a string => " + numChain[-2:])

sequentialNumChain = "1234567890"
print("get the sub string skipping every nth number => " + sequentialNumChain[2:7:2])
print("syntax: string[<start index>:<end index>:<skip count>")

print("")
print(f"To reverse a string => "+sequentialNumChain[::-1])
print(f"To reverse a string getting every other element=> "+sequentialNumChain[::-2])
print("syntax/clarification: string[<NO START INDEX>:<NO END INDEX>: <skip backwards by one")

print("")
print(f"To set Hello World to upper and lower => " + "Hello World".upper() + " to lower " + "Hello World".lower())
print("syntax to set to upper and lower case we use .upper() and .lower()")

print("")
print("check if string starts or ends with a value")
print(f"{sequentialNumChain} starts with 123 => {sequentialNumChain.startswith('123')}")
print(f"{sequentialNumChain} starts with 890 => {sequentialNumChain.endswith('890')}")

print("")
print("Split on space ' ' => ", sequentialNumChain.split("5"))
print("syntax 'string.split('value') returns a list")