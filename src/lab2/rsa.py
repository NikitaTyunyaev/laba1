
def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(pow(n,0.5)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    # 1 часть
    a, b = e, phi
    table = []
    while a != 0 and b != 0:
        table.append([a, b, a % b, a // b])
        a, b = b, a % b
    # 2 часть
    x, y = 0, 1
    for i in range(len(table) - 2, 0, -1):
        x, y = y, x - y * table[i][3]
    return y % phi