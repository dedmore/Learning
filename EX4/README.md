Exercise 4, Variables And Names. This exercise shows how easy setting up variables is. Using variable names help to organize your code and make it easier to keep track of what’s going on in the program.

Study Drills:

Explain this error in your own works. Make sure you use line numbers and explain why.

Traceback (most recent call last):
      File "ex4.py", line 8, in <module>
        average_passengers_per_car = car_pool_capacity / passenger
    NameError: name 'car_pool_capacity' is not defined

This error tells me that on line 8 of ex4.py the variable car_pool_capacity has not been initialized with any value.

1.	I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?

2.	Remember that 4.0 is a "floating point" number. Find out what that means.

3.	Write comments above each of the variable assignments.

4.	Make sure you know what = is called (equals) and that it's making names for things.

5.	Remember that _ is an underscore character.

6.	Try running python as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.

In response to #1, I don’t feel that it’s necessary and after making the change in the code the value of carpool_capacity becomes 120 instead of 120.0. #2, The term floating point is derived from the fact that there is no fixed number of digits before and after the decimal point; that is, the decimal point can float. #3, ex4-commented.py. #4, The = (single-equal) assigns the value on the right to a variable on the left. #5, _ is an underscore character. #6, ex4-calculatevariablesused.py
