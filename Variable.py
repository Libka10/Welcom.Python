#Assignment statements create new variables and also give them values to refer to.

message = "What's up, Doc?"
n = 17
pi = 3.14159

caasimaduwaa ="HARGEISA"

print(caasimaduwaa)



print(message)
print(n)
print(pi)

#Note always the last variable value assigned will come out when print! EG

day = "Thursday"
day = 32.5
day = 19

print(day)
 
 # Here 19 will pop up actually.




 # If you give a variable an illegal name, you get a syntax error. In the example below, each of the variable names is illegal.

# 76trombones = "big parade"
# more$ = 1000000
# class = "Computer Science 101"
# 76trombones is illegal because it does not begin with a letter. 
# more$ is illegal because it contains an illegal character, the dollar sign. But what’s wrong with class?

# It turns out that class is one of the Python keywords. Keywords define the language’s syntax rules and structure,
#  and they cannot be used as variable names. 
# Python has thirty-something keywords (and every now and again improvements to Python introduce or eliminate one or two). 
# This list is current as of Python.


# 76trombones is illegal because it does not begin with a letter. more$ is illegal because it contains an illegal character, the dollar sign. But what’s wrong with class?

#It turns out that class is one of the Python keywords.
# Keywords define the language’s syntax rules and structure, 
# and they cannot be used as variable names. 
# Python has thirty-something keywords (and every now and again improvements to Python introduce or eliminate one or two). 
# This list is current as of Python version 
  
 # As we have mentioned previously, it is legal to make more than one assignment to the same variable. 
# A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

bruce = 5
print(bruce)
bruce = 7
print(bruce)

Laahiq = 2
print(Laahiq + 10)

#It is important to note that in mathematics, a statement of equality is always true.
#If a is equal to b now, then a will always equal to b.
#In Python, an assignment statement can make two variables refer to the same object and therefore have the same value.
#They appear to be equal. However, 
#because of the possibility of reassignment, 
#they don’t have to stay that way:

a = 5
b = a    # after executing this line, a and b are now equal
print(a,b)
a = 3    # after executing this line, a and b are no longer equal
print(a,b)


# After the following statements, what are the values of x and y?

x = 15
y = x
x = 22

# A. x is 15 and y is 15
# B. x is 22 and y is 22
# C. x is 15 and y is 22
# D. x is 22 and y is 15   #D will be the anwsere because x has changed its value to 22 !

print(x,y)
print(y,x)