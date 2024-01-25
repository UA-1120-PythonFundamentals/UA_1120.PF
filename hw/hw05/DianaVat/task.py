# list_int = [ 1 , 2, 3, 4]  
# list_two = []
# for x in list_int:
#     list_two.append(float(x))
# list_int = list_two
# print(list_int)
# #Create function for list (int to float)


# enter = int(input("Enter your number for Fibonacci: "))
# oneFib = 0
# twoFib = 1
# step = 1
# fibonacci = 1
# while step < enter:
#     fibonacci = oneFib + twoFib
#     oneFib = twoFib
#     twoFib = fibonacci
#     step+=1
# print(fibonacci)
# #Create loop for Fibonacci


enter = int(input("Enter your number for factorial : "))
factorial = 1
while enter >1:
    factorial *=enter
    enter -= 1
print(factorial)
 #Create script for factorial