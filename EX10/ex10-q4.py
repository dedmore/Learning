var1 = "I am 6'2\" tall." # Escape double-quote inside string
var2 = 'I am 6\'2" tall.' # Escape single-quote inside string

# Print test: followed by raw data of var1
print  "test: %r" % var1
# Print test: followed by string data of var1
print  "test: %s" % var1
# Print test: followed by raw data of var2
print  "test: %r" % var2
# Print test: followed by string data of var2
print  "test: %s" % var2