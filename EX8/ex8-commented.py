# Defines formatter as a string with four raw data formatters
formatter = "%r %r %r %r"

# Prints formatter to screen using following data
print formatter % (1, 2, 3, 4)
# Prints formatter to screen using following data
print formatter % ("one", "two", "three", "four")
# Prints formatter to screen using following data
print formatter % (True, False, False, True)
# Prints formatter to screen using following data
print formatter % (formatter, formatter, formatter, formatter)
# Prints formatter to screen using following data
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)