def celsius_to_fahrenheit(temps):
    def convert_temp(celsius):
        return (celsius * 9/5) + 32
    
    return list(map(convert_temp, temps))

def combinations(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)

def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  

def celsius_to_fahrenheit(temps):
    return [(temp * 9/5) + 32 for temp in temps]

def add_tag(tag):
    def decorator(func):
        def wrapper():
            message = func()
            return f"{tag}{message}{tag}"
        return wrapper
    return decorator