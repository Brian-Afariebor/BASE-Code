# How to use BASE-Code

# Printing Items 

To print a line, type the keyword "print", followed the line.

Example)

print Hello World! \ end >>> print("Hello World!")

# Getting User Input 

To get the user's input, use the keyword "input".

Example) 

print \ input \ end >>> print(input(" "))

# Running Functions in another Function

In some cases, running a function in another function is neccassary to keep things going smoothly.

# Defining Items 

To define an item, use the "item" keyword, follwed by "\ set" for the value.

Examples ) 

item x \ set 1 >>> x = 1

item x \ input \ set 1 >>> x[input] = 1

# Defining Locations

In BASE-Code, there are 2 types of Locations: Points, written using "point", and Constants, written using "const". Points are always run if the program gets to them, and Constants are only run if they are called. However, if they reference another Constant or Point, said Constant or Point should have already been defined by the program.
As a result, Constants are used to effectively make functions, and Points for simple loops and conditionals.

Example )

... 
point 1 >>> locations[points][1] = CODE1
CODE1
...
const 1>>> locations[constants] = CODE2
CODE2
...

# Going to a location 

To go to a point, use the "go" keyword, and then type the Point name. To go to a specific word, add the keyword "word", and then type the word number(the first word is word 0). To go to the top of the Go Stack, add the "top" keyword.

Examples )

go 1 >>> Pointer = Point[1]

go word 1 >>> Pointer = 1

go top >>> Pointer = go.add(Point[Points[Length]]-1)

# Adding a defined Point to the Go Stack 

To add a point to the Go Stack, add the "add" keyword, and then type the Point name. To add a specific word, add the keyword "word", and then type the word number(the first word is 0).

Examples ) 

add 1 >>> go.append(point[1]) 

add word 1 >>> go.append(1)
