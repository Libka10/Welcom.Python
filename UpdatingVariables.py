# One of the most common forms of reassignment is an update where the new value of the variable depends on the old. For example,
# x = x + 1

# This means get the current value of x, add one, and then update x with the new value. The new value of x is the old value of x plus 1.
#  Although this assignment statement may look a bit strange, remember that executing assignment is a two-step process.
#  First, evaluate the right-hand side expression. Second, 
# let the variable name on the left-hand side refer to this new resulting object.
#  The fact that x appears on both sides does not matter. 
# The semantics of the assignment statement makes sure that there is no confusion as to the result. 
# The visualizer makes this very clear.

x= 6
x = x + 1

x = 6            #initialize
print(x)

x = x + 1    # update x
print(x)



# If you try to update a variable that doesn’t exist, 
# you get an error because Python evaluates the expression on the right side of the assignment operator before it assigns the resulting value to the name on the left.
#  Before you can update a variable, you have to initialize it, 
# usually with a simple assignment.
#  In the above example, x was initialized to 6.

# Updating a variable by adding something to it is called an increment; 
# subtracting is called a decrement.
#  Sometimes programmers talk about incrementing or decrementing without specifying by how much;
#  when they do they usually mean by 1.
#  Sometimes programmers also talk about bumping a variable,
#  which means the same as incrementing it by 1.

# Incrementing and decrementing are such common operations that programming languages often include special syntax for it. 
# In Python += is used for incrementing, and -= for decrementing.
#  In some other languages, there is even a special syntax ++ and -- for incrementing or decrementing by 1.
#  Python does not have such a special syntax. 
# To increment x by 1 you have to write x += 1 or x = x + 1.


x = 6        # initialize x
print(x)
x += 3       # increment x by 3; same as x = x + 3
print(x)
x -= 1       # decrement x by 1
print(x)


#Imagine that we wanted to not increment by one each time but instead add together the numbers one through ten, but only one at a time.

s = 1
print(s)
s = s + 2
print(s)
s = s + 3
print(s)
s = s + 4
print(s)
s = s + 5
print(s)
s = s + 6
print(s)
s = s + 7
print(s)
s = s + 8
print(s)
s = s + 9
print(s)
s = s + 10
print(s)


#After the initial statement, where we assign s to 1,
# we can add the current value of s and the next number that we want to add (2 all the way up to 10) 
# and then finally reassign that that value to s so that the variable is updated after each line in the code.

#This will be tedious when we have many things to add together. 
# Later you’ll read about an easier way to do this kind of task.

# What is printed when the following statements execute?

x = 12
x = x - 1
print(x)


# A. 12
# B. -1
# C. 11            #The anwsere is c !
# D. Nothing. An error occurs because x can never be equal to x - 1.
