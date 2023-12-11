print("Hello, world")
input("what's your name? ")
#space after ? for aesthetics
name = input("what's your name? ")
#remove white space from string, function from the documentation
name = name.strip()
#capitalize user's name
name = name.capitalize()
#One argument, need space after hello,
print("Hello, " + name)
#or with two arguments 
print("Hello,",name)
print("Hello,",name)
print ("Hello,")
print(name)
# docs.python.org/3/library/functions.html    -    Python documentation with all the functions!!!
# print (*objects, sep= ' ', end ='\n' , file=sys.stdout, flush = false) --> print fucntion from the python documentation
# so to make everything in one line you can change end ='\n' to end ='' !!!!
print("Hello, " , end = '')
print (name)
print ("Hello, 'friend'")
#or
print ('Hello, "friend"')
#or, back slash = escape char, comp will know that it is literally a " not the command
print ("Hello, \"friend\"")
print (f"Hello, {name}")
