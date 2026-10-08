def _check_int(value, name):
    """Lanza TypeError si value no es un entero (bool no cuenta como entero)."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{name} debe ser un número entero")


def square(n):
    """Retorna el cuadrado de un número."""
    if not isinstance(n, (int, float)) or isinstance(n, bool):
        raise TypeError("n debe ser un número")
    return n * n


def factorial(n):
    """Retorna el factorial de un número entero no negativo."""
    _check_int(n, "n")
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """Retorna True si n es primo, False en caso contrario."""
    _check_int(n, "n")
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a, b):
    """Retorna el máximo común divisor de a y b (algoritmo de Euclides)."""
    _check_int(a, "a")
    _check_int(b, "b")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Retorna el mínimo común múltiplo de a y b."""
    _check_int(a, "a")
    _check_int(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    print("square(5) =", square(5))
    print("factorial(5) =", factorial(5))
    print("is_prime(17) =", is_prime(17))
    print("gcd(48, 18) =", gcd(48, 18))
    print("lcm(4, 6) =", lcm(4, 6))
