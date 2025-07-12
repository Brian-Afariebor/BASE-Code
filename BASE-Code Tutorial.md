# How to use BASE-Code

# Printing Items 

To print a line, type the keyword "print", followed the line.

Example )

print Hello World! \ end >>> print("Hello World!")

# Getting User Input 

To get the user's input, use the keyword "input".

Example ) 

print \ input \ end >>> print(input(" "))

# Running Functions in another Function

In some cases, running a function in another function is neccassary to keep things going smoothly. To run a function in another function, type "\", followed by the function name. There are, however, special functions that modifiy or slightly change the result of a function. They are:

\ n (or \ null) : writes a null valued string (think of it as a space) to the Data Stack

\ \ : writes the backslash "\ " to the Data Stack

\ then : ends the current function and runs the next one (think of it like a semicolon, ";")

\ end : ends the current function and then stops the program

\ to : ends the current function and keeps it's result in the Data Stack

\ set : sets the value of the item path to the result of the next function

If the backslash is not followed by a valid function, it will be used as a regular backslash without it's properties.

Example )

item name \ set >>> name = ?

   input \ then >>> name = input; 

print \ item name \ then >>> print(name);

print \ : this is a backslash \ end >>> print("\ : this is a backslash");

# Defining Items 

To define an item, use the "item" keyword, follwed by typing the corresponding function "\ set" to set the value.

Examples ) 

item x \ set >>> x = ?
  1 \ then >>> x = 1;

item x \ input \ set 
  1 \ then >>> x[input] = 1;

# Defining Locations

In BASE-Code, there are 2 types of Locations: Points, written using "point", and Constants, written using "const" or "constant". Points are always run if the program gets to them, and Constants are only run if they are called. However, if they reference another Constant or Point, said Constant or Point should have already been defined by the program.
As a result, Constants are used to effectively make callable functions, and Points for simple loops and conditionals.

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

To go to a point or constant, use the "goto" keyword, and then type Point or Constant, followed by it's name. To go to the top of the Go Stack, add the "last" keyword. You cannot go to a place that hasn't been defined yet, unless you add the keyword "general" to the name. The code will then go to the first point it finds, from the top, that has that name. If it doesn't find it, it will stop the program. Note that using "general" will cause a significant delay in the execution of the destination.

Examples )

goto point 1 >>> Pointer = locations[point][1]

goto const 2 >>> Pointer = locations[constant][1]

goto last >>> Pointer = Pointer = locations[locations0]]

goto global point 1 >>> repeat untill locations[current] = 1 : Pointer ++; then: locations[point][1] = locations[current]

# Adding a defined Point to the Go Stack 

To add a point to the Go Stack, add the "add" keyword, and then type the Point or Constant name. If you would like to save the current point or constant, type "current".

Examples ) 

add 1 >>> goto.append(locations[point][1]) 

add current >>> goto.append(locations[current])
