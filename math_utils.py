def _check_int(value, name):
    """Lanza TypeError si value no es un entero (bool no cuenta como entero)."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{name} debe ser un número entero")


def _check_number(value, name):
    """Lanza TypeError si value no es int o float (bool no cuenta como número)."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{name} debe ser un número")


def square(n):
    """Retorna el cuadrado de un número."""
    _check_number(n, "n")
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


def cube(n):
    """Retorna el cubo de un número."""
    _check_number(n, "n")
    return n * n * n


def power(base, exponent):
    """Retorna base elevado a un exponente entero no negativo."""
    _check_number(base, "base")
    _check_int(exponent, "exponent")
    if exponent < 0:
        raise ValueError("exponent debe ser un entero no negativo")
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def sqrt(n):
    """Retorna la raíz cuadrada de un número no negativo."""
    _check_number(n, "n")
    if n < 0:
        raise ValueError("n no puede ser negativo")
    return n ** 0.5


def is_even(n):
    """Retorna True si n es par, False si es impar."""
    _check_int(n, "n")
    return n % 2 == 0


def fibonacci(n):
    """Retorna el n-ésimo número de Fibonacci (fibonacci(0) = 0)."""
    _check_int(n, "n")
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def divide(a, b):
    """Retorna el cociente a / b."""
    _check_number(a, "a")
    _check_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("no se puede dividir entre cero")
    return a / b


def mean(numbers):
    """Retorna el promedio de una lista de números."""
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("numbers debe ser una lista o tupla")
    if not numbers:
        raise ValueError("numbers no puede estar vacía")
    for value in numbers:
        _check_number(value, "cada elemento")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("square(5) =", square(5))
    print("factorial(5) =", factorial(5))
    print("is_prime(17) =", is_prime(17))
    print("gcd(48, 18) =", gcd(48, 18))
    print("lcm(4, 6) =", lcm(4, 6))
    print("cube(3) =", cube(3))
    print("power(2, 10) =", power(2, 10))
    print("sqrt(16) =", sqrt(16))
    print("is_even(8) =", is_even(8))
    print("fibonacci(10) =", fibonacci(10))
    print("divide(7, 2) =", divide(7, 2))
    print("mean([1, 2, 3, 4]) =", mean([1, 2, 3, 4]))
