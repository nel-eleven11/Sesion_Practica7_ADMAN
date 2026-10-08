import unittest

from math_utils import (
    cube,
    divide,
    factorial,
    fibonacci,
    gcd,
    is_even,
    is_prime,
    lcm,
    mean,
    power,
    sqrt,
    square,
)

# test de pr 1
class TestSquare(unittest.TestCase):
    def test_entero_positivo(self):
        self.assertEqual(square(5), 25)

    def test_entero_negativo(self):
        self.assertEqual(square(-4), 16)

    def test_flotante(self):
        self.assertAlmostEqual(square(1.5), 2.25)

    def test_cero(self):
        self.assertEqual(square(0), 0)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            square("3")


class TestFactorial(unittest.TestCase):
    def test_numero_pequeno(self):
        self.assertEqual(factorial(5), 120)

    def test_numero_mayor(self):
        self.assertEqual(factorial(10), 3628800)

    def test_cero(self):
        self.assertEqual(factorial(0), 1)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_flotante(self):
        with self.assertRaises(TypeError):
            factorial(3.5)


class TestIsPrime(unittest.TestCase):
    def test_primos(self):
        for n in (2, 3, 5, 7, 13, 97):
            with self.subTest(n=n):
                self.assertTrue(is_prime(n))

    def test_no_primos(self):
        for n in (4, 9, 15, 25, 100):
            with self.subTest(n=n):
                self.assertFalse(is_prime(n))

    def test_menores_que_dos(self):
        for n in (-7, 0, 1):
            with self.subTest(n=n):
                self.assertFalse(is_prime(n))

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            is_prime("7")


class TestGcd(unittest.TestCase):
    def test_caso_basico(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_coprimos(self):
        self.assertEqual(gcd(17, 5), 1)

    def test_con_cero(self):
        self.assertEqual(gcd(0, 9), 9)

    def test_negativos(self):
        self.assertEqual(gcd(-12, 8), 4)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            gcd(4.0, 2)


class TestLcm(unittest.TestCase):
    def test_caso_basico(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_coprimos(self):
        self.assertEqual(lcm(3, 7), 21)

    def test_con_cero(self):
        self.assertEqual(lcm(0, 5), 0)

    def test_negativos(self):
        self.assertEqual(lcm(-4, 6), 12)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            lcm("4", 6)


class TestCube(unittest.TestCase):
    def test_entero_positivo(self):
        self.assertEqual(cube(3), 27)

    def test_entero_negativo(self):
        self.assertEqual(cube(-2), -8)

    def test_flotante(self):
        self.assertAlmostEqual(cube(1.5), 3.375)

    def test_cero(self):
        self.assertEqual(cube(0), 0)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            cube("3")


class TestPower(unittest.TestCase):
    def test_potencia_de_dos(self):
        self.assertEqual(power(2, 10), 1024)

    def test_base_negativa(self):
        self.assertEqual(power(-3, 3), -27)

    def test_base_flotante(self):
        self.assertAlmostEqual(power(0.5, 2), 0.25)

    def test_exponente_cero(self):
        self.assertEqual(power(7, 0), 1)

    def test_exponente_negativo(self):
        with self.assertRaises(ValueError):
            power(2, -1)

    def test_exponente_flotante(self):
        with self.assertRaises(TypeError):
            power(2, 1.5)


class TestSqrt(unittest.TestCase):
    def test_cuadrado_perfecto(self):
        self.assertEqual(sqrt(16), 4)

    def test_no_perfecto(self):
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=6)

    def test_cero(self):
        self.assertEqual(sqrt(0), 0)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            sqrt(-4)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            sqrt("16")


class TestIsEven(unittest.TestCase):
    def test_pares(self):
        for n in (0, 2, 8, -4, 100):
            with self.subTest(n=n):
                self.assertTrue(is_even(n))

    def test_impares(self):
        for n in (1, 7, -3, 99):
            with self.subTest(n=n):
                self.assertFalse(is_even(n))

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            is_even(2.0)


class TestFibonacci(unittest.TestCase):
    def test_primeros_valores(self):
        esperados = [0, 1, 1, 2, 3, 5, 8, 13]
        for n, valor in enumerate(esperados):
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), valor)

    def test_valor_mayor(self):
        self.assertEqual(fibonacci(30), 832040)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            fibonacci("5")


class TestDivide(unittest.TestCase):
    def test_division_exacta(self):
        self.assertEqual(divide(10, 2), 5)

    def test_division_con_decimales(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_negativos(self):
        self.assertEqual(divide(-9, 3), -3)

    def test_entre_cero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            divide("10", 2)


class TestMean(unittest.TestCase):
    def test_enteros(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_flotantes_y_tupla(self):
        self.assertAlmostEqual(mean((1.5, 2.5, 3.5)), 2.5)

    def test_un_elemento(self):
        self.assertEqual(mean([7]), 7)

    def test_lista_vacia(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_elemento_invalido(self):
        with self.assertRaises(TypeError):
            mean([1, "2", 3])

    def test_no_es_lista(self):
        with self.assertRaises(TypeError):
            mean(5)


if __name__ == "__main__":
    unittest.main()
