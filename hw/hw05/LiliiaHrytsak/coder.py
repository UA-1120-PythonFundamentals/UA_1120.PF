def mean(number):
    if number < 10:
        return number
    else:
        sum_n = 0
        k = 0

        while number > 0:
            sum_n += number % 10
            k += 1
            number //= 10

        return int(round(sum_n / k, 0))
print(mean(1024))