"""Opción A: funciones de matemática básica."""


def square(n):
    """Retorna el cuadrado de un número."""
    return n * n


def factorial(n):
    """Retorna el factorial de un número entero no negativo."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n debe ser un número entero")
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """Retorna True si n es primo, False en caso contrario."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n debe ser un número entero")
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
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Retorna el mínimo común múltiplo de a y b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    print("square(5) =", square(5))
    print("factorial(5) =", factorial(5))
    print("is_prime(17) =", is_prime(17))
    print("gcd(48, 18) =", gcd(48, 18))
    print("lcm(4, 6) =", lcm(4, 6))
