def find_min_max(data):
    min_value = max_value = data[0]
    for i, value in enumerate(data):
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value
    return max_value, min_value


def fibonacci(max_times):
    n, a, b = 0, 0, 1
    while n < max_times:
        yield b
        a, b = b, a + b
        n = n + 1
    return "Done"


def yang_hui_triangle(n):
    max_line = 1
    next_line = [1, 1]
    while max_line <= n:
        if max_line == 1:
            yield [1]
        else:
            temp = next_line.copy()
            yield temp
            next_line.clear()
            for i, v in enumerate(temp):
                if i < len(temp) - 1:
                    next_line.insert(i + 1, temp[i] + temp[i + 1])
            next_line.insert(0, 1), next_line.append(1)
        max_line = max_line + 1
    return next_line


def format_name(name):
    new_name = ""
    for i, v in enumerate(name):
        if i == 0:
            new_name = new_name + v.upper()
        else:
            new_name = new_name + v.lower()
    return new_name


def prod(values):
    from functools import reduce
    return reduce(lambda x, y: x * y, values)


def prod2(values):
    from functools import reduce

    def multi(x, y):
        return x * y

    return reduce(multi, values)


def normalize(value):
    if isinstance(value, str):
        return value.capitalize()


def str2float(value):
    from functools import reduce

    digits = {'.': -1, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(char):
        return digits[char]

    def count_decimal(float_value):
        if float_value == int(float_value):
            return 0
        return len(str(float_value).split('.')[1])

    def num2float(x, y):
        if isinstance(x, int):
            if y == -1:
                return float(x)
            else:
                return x * 10 + y
        elif isinstance(x, float):
            return x + y * 10 ** -(count_decimal(x) + 1)

    return reduce(num2float, map(char2num, list(value)))


def is_palindrome(n):
    n_str = str(n)
    length = len(n_str)
    for index in range(length):
        if index < length / 2:
            if n_str[index] == n_str[length - 1 - index]:
                continue
            else:
                return False
        else:
            return True


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


def create_counter2():
    e = 0

    def next_num():
        global e
        e += 1
        return e

    return next_num


def log(func):
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now(time):
    print('now is: ' + time)


def h_log(text):
    def decorator(func):
        import functools

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(text + ' call %s():' % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@h_log('Happy')
def h_now():
    print('now is tomorrow.')


def metric(func):
    import time
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('%s() executed in %ss' % (func.__name__, end - start))
        return result
    return wrapper


@metric
def fast():
    import time
    time.sleep(0.1)
    return 'Done'
