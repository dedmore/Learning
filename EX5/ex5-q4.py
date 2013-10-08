name = 'Brandon C. Dedmore'
age = 30
height = 72 #inches (6 * 12)
centimeter = 2.54 # 1 inch is equal to 2.54 centimeter
heightcm = height * centimeter
weight = 200 # lbs
kilogram = .453592 # 1 pound is equal to .453592 Kilograms
weightkg = weight * kilogram
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "Or %r centimeters." % heightcm
print "He's %r pounds heavy." % weight
print "Or %r Kilograms." % weightkg
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)