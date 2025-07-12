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

...

const 2 >>> locations[constants][2] = CODE2

CODE2

...

# Going to a location 

To go to a point or constant, use the "goto" keyword, and then type Point or Constant, followed by it's name. To go to the top of the Go Stack, add the "last" keyword.

Examples )

go point 1 >>> Pointer = Point[1]

goto last >>> Pointer = goto.add(Point[Points[Length]]-1)

# Adding a defined Point to the Go Stack 

To add a point to the Go Stack, add the "add" keyword, and then type the Point or Constant name. If you would like to save the current place, type "current".

Examples ) 

add 1 >>> goto.append(locations[point][1]) 

add current >>> goto.append(pointer)
