def is_armstrong_number(number):
    n = number
    digits = [int(d) for d in str(n)]
    power = len(digits)
    value = 0
    for i in digits:
        value += i ** power
    if value == n:
        return True
    else:
        return False
        
