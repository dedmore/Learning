# Defines x as a string that has a decimal value inside
x = "There are %d types of people." % 10
# Defines binary as a string with text
binary = "binary"
# Defines do_not as a string with text
do_not = "don't"
# Defines y as a string with two strings inside
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the value of x
print x
# Prints the value of y
print y

# Prints "I said: " followed by the raw data output value of x
print "I said: %r." % x
# Prints "I also said: " followed by the string data value of y
print "I also said: '%s'." % y

# Defines hilarious as False
hilarious = False
# Defines joke_evaluation with string information followed by raw data output of not yet defined variable
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the value of joke_evaluation followed by the raw data output of variable hilarious
print joke_evaluation % hilarious

# Defines w as a string with text
w = "This is the left side of..."
# Defines e as a string with text
e = "a string with a right side."

# Prints the value of w followed by the value of e
print w + e