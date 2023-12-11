import math

def perfect_square(user_input):
    sqrt_num = math.isqrt(user_input)
    return sqrt_num * sqrt_num == user_input

def tricky_square(num):
    if not perfect_square(num):
        return False

    number = str(num)
    digit_count = [0] * 10

    for digit in number:
        digit_count[int(digit)] += 1

    repeated = 0
    for count in digit_count:
        if count > 1:
            repeated += 1

    return repeated == 1

def count_tricky_squares(a, b):
    count = 0
    for num in range(a, b + 1):
        if perfect_square(num) and tricky_square(num):
            count += 1
    return count

a, b = map(int, input().split())
result = count_tricky_squares(a, b)
print(result)
