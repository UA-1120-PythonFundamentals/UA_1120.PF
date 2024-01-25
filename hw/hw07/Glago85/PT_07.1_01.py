#Write a function that returns the largest number of two numbers 
#(use DocStrings documentation strings in the function).
def maximum(x, y):
    '''Function, that returns the largest number of two numbers'''
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return str(f"The numbers are equal {x}")