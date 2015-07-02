def greatest_common_divisor(*args):
    data = list(args)
    x = data.pop(0)
    for i in data:
        if x > i: x = gcd(x, i)
        else: x = gcd(i, x)
    return x

def gcd(x, y):
    if y == 0: return x
    else: return gcd(y, x % y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"

