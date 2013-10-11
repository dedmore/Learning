# Prints "How old are you?" to the screen
print "How old are you?",
# Creates variable age with input from keyboard
age = raw_input()
# Prints "How tall are you?" to the screen
print "How tall are you?",
# Creates variable height with input from keyboard
height = raw_input()
# Prints "How much do you weigh?" to the screen
print "How much do you weigh?",
# Creates variable weight with input from the keyboard
weight = raw_input()

# Prints string with three variables inside
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)