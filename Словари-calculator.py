def calc(expr):
    allowed = '+-*/'
    if not any(sign in expr for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы 1 знак ({allowed})')
    for sign in allowed:
        if sign in expr:
            try:
                left, right = expr.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')


if __name__ == '__main__':
    print(calc('10*5'))
