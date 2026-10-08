import unittest

from math_utils import factorial, gcd, is_prime, lcm, square


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


if __name__ == "__main__":
    unittest.main()
