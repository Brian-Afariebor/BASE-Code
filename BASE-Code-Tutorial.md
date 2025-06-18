# How to use BASE-Code

# Printing Items 

To print a line, type the keyword "print", followed the line. If you would like to print the result of a fuction, type a  backslash (\), followed by the function.

Exs. print Hello World! \ end >>> print("Hello World!"); print \ n \ end >>> print(" "); print Good! \ go 1 >>> print("Good!"), function_at_1()

# Getting User Input 

To get the user's input, use the keyword "inpu".

Exs. print input \ end >>> print(input(" "))

# Defining Items 

To define an item, use the "item" keyword, follwed by "set" for the value.

Exs: item x set 1 >>> x = 1; item x input set 1 >>> x[input] = 1

# Defining Points 

In BASE-Code, functions are run by going to a point, and then comming back, similar to ASM. To set a point to goto, use the keyword "point", and then type the number to set the point.

Ex: point 1 CODE >>> Point[1] = CODE

# Going to a Point 

To go to a point, use the "go" keyword, and then type the Point name. To go to a specific word, add the keyword "word", and then type the word number(the first word is word 0). To go to the top of the Go Stack, add the "top" keyword.

Exs: go 1 >>> Pointer = Point[1]; go word 1 >>> Pointer = 1; go top >>> Pointer = go[len(go)-1]

# Adding a defined Point to the Go Stack 

To add a point to the Go Stack, add the "add" keyword, and then type the Point name. To add a specific word, add the keyword "word", and then type the word number(the first word is 0).

Exs: add 1 >>> go.append(point[1]); add word 1 >>> go.append(1)
