def fizz_buzz(n):
    li = []
    for x in range(1, n + 1):
        if x % 15 == 0:
            li.append("FizzBuzz")
        elif x % 5 == 0:
            li.append("Fizz")
        elif x % 3 == 0:
            li.append("Buzz")
        else:
            li.append(x)
    #with open('test.txt', 'w') as f:
    #    file = f.write("\n".join(str(li).split(',')))
    return li


def fibonacci(n):
    # 1 1 2 3 5 8 13
    if n <= 0:
        return 0
    i = 1
    n1, n2 = 0, 1
    while i < n:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1
    return n2


def fibonacci_for(n):
    n1, n2 = 0, 1
    nth = 0
    if n <= 0:
        return 0
    for x in range(1, n):
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return n2


def check_palindrom(word):
    return word.lower() == word.lower()[::-1]


def is_prime(n):
    if n <= 1:
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


def is_prime_2(n):
    return n > 1 and [x for x in range(2, n) if n % x == 0] == []


def money_quiz(n):
    # 1, 2, 5
    dct = {'5zl': 0, '2zl': 0, '1zl': 0}
    if n // 5 > 0:
        dct['5zl'] = n // 5
        n -= n // 5 * 5
    if n // 2 > 0:
        dct['2zl'] = n // 2
        n -= n // 2 * 2
    if n == 1:
        dct['1zl'] = 1
    return dct


def bubble_sort(li):
    # [2, 3, 4, 1]
    for x in range(len(li)):
        for y in range(len(li) - 1):
            if li[y] > li[y + 1]:
                temp = li[y + 1]
                li[y + 1] = li[y]
                li[y] = temp
    return li

