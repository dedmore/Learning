x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# This is the first and second spot where a string is inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# This is the third spot
print "I said: %r." % x
# This is the forth spot
print "I also said: '%s'." % y

hilarious = False
# This may be a fifth spot depending on how you look at hilarious as a variable, if looked at as a string, maybe not if looked at as boolean values
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e