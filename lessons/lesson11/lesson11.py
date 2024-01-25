# number = None

 
# try:
#     number = int(input("enter number:"))
# except: 
#     number = 0

# print(number)

# a = b =  c = None
# try:
#     numbers = input("enter a b c")
#     a, b, c = map(int, numbers.split())
#     d = b**2 -4*a*c
#     x1 = (-b+d**0.5)/(2*a)
#     x2 = (-b-d**0.5)/(2*a)

# except ValueError:
#     print("error")
# except (ZeroDivisionError, KeyError) as err:
#     print("ZeroDivisionError") 
# except Exception as err:
#     print("Exception", type(err), err)
# else:
#     print(f"{x1=}, {x2=}")
# finally:
#     print("finally")

# print("end")

# def div(a, b):
#     try:
#         return a/b
#     except:
#         return 0
#     finally:
#         # return ">0<"
#         print("finally")
    
# print(div(1, 2))
# print(div(1, 0))

# def read_int(text, min=None, max=None):
#     while True:
#         try:
#             result = int(input(text))
#             if min is not None and result < min:
#                 continue
#             if max is not None and result > max:
#                 continue
#             return result
#         except:
#             print("Input should be int")

# # a =  read_int("x:")
# # print(a)
# a =  read_int("x:", 5, 25)
# print(a)


# def read_int(text, min=None, max=None):
#     while True:
        
#         try:
#             result = int(input(text))
#             if min is not None and result < min:
#                 raise ArithmeticError(f"value {result} < {min}")
#             if max is not None and result > max:
#                 raise KeyError(f"value {result} > {max}")
#             return result
#         except ArithmeticError as err:
#             print("err1:", err)
#         except KeyError as err:
#             print("err2:", err)
#         except:
#             print("Input should be int")

# # a =  read_int("x:")
# # print(a)
# a =  read_int("x:", 5, 25)
# print(a)


class MinValueError(Exception): pass
class MaxValueError(Exception): pass
    

# def read_int(text, min=None, max=None):
#     while True:
        
#         try:
#             result = int(input(text))
#             if min is not None and result < min:
#                 raise MinValueError(f"value {result} < {min}")
#             if max is not None and result > max:
#                 raise KeyError(f"value {result} > {max}")
#             return result
#         except MinValueError as err:
#             print("MinValueError:", err)
#         except MaxValueError as err:
#             print("MaxValueError:", err)
#         except:
#             print("Input should be int")

# # a =  read_int("x:")
# # print(a)
# a =  read_int("x:", 5, 25)
# print(a)

# import logging


# logging.basicConfig(level=logging.INFO,
#                     filename='app.log',
#                     filemode='a',
#                     format='%(name)s %(asctime)s -[ %(process)d, %(processName)s]  %(funcName)s %(levelname)s - %(message)s')
from log import logging
def f():
    logging.error('This is a f-debug message')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

f()