# Sesión Práctica 7: Integración continua

Este repositorio practica el uso de Git, pruebas unitarias e integración continua con GitHub Actions. La opción seleccionada es **matemática básica**. La librería implementa `square`, `factorial`, `is_prime`, `gcd` y `lcm`; también contiene funciones adicionales (`cube`, `power`, `sqrt`, `is_even`, `fibonacci`, `divide` y `mean`) con sus respectivas pruebas.

## Ejecutar las pruebas

Se requiere Python 3.12 o compatible. Desde la raíz del repositorio, ejecuta:

```bash
python -m unittest discover -s tests -t . -v
```

Las pruebas cubren resultados esperados, casos límite y entradas no válidas. Para cada función seleccionada hay varios casos exitosos y casos de error.

## Integración continua y Pull Requests

El workflow de GitHub Actions, en `.github/workflows/tests.yml`, ejecuta la suite cuando se suben cambios a `main` o `develop`, y cuando se abre o actualiza un Pull Request hacia esas ramas. El ruleset de `main` requiere que pase el check **Unit tests** antes de permitir el merge.

Flujo habitual para proponer cambios:

1. Crea o usa una rama de trabajo y realiza los cambios allí.
2. Ejecuta las pruebas localmente con el comando anterior.
3. Sube la rama y abre un Pull Request hacia `main`.
4. Espera a que **Unit tests** termine correctamente; si falla, corrige el problema y vuelve a subir los cambios.
5. Cuando el check pase, GitHub habilitará el merge de acuerdo con las reglas de la rama.

## Demostración en vivo: prueba fallida y corrección

Para demostrar el bloqueo, modifica temporalmente la función `square` en `math_utils.py` de esta forma. La suma reemplaza deliberadamente el cálculo correcto y hace que varias pruebas fallen:

```python
def square(n):
    """Retorna el cuadrado de un número."""
    _check_number(n, "n")
    return n + n  # Cambio temporal: las pruebas deben fallar.
```

Sube el cambio a la rama del Pull Request y verifica que **Unit tests** falle y que el merge quede bloqueado. Para corregirlo y permitir que el PR apruebe, restaura la multiplicación:

```python
def square(n):
    """Retorna el cuadrado de un número."""
    _check_number(n, "n")
    return n * n
```

Sube la corrección al mismo Pull Request. Cuando **Unit tests** pase, el merge quedará habilitado.
