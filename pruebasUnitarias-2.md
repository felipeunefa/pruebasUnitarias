# Pruebas odoo

Hay muchas formas de probar una aplicación. En Odoo, tenemos tres tipos de pruebas.

- Pruebas unitarias de python: útiles para probar la lógica de negocios del modelo
- Pruebas unitarias js: esto es necesario para probar el código javascript de forma aislada
- Recorridos: esta es una forma de prueba de integración. Los recorridos aseguran que las partes de python y javascript se comuniquen entre sí correctamente.

## Prueba de código Python

Odoo proporciona soporte para probar módulos usando unittest.

Para escribir `tests`, simplemente defina un subpaquete de pruebas en su módulo, se inspeccionará automáticamente en busca de módulos de prueba. Los módulos de prueba deben tener un nombre que comience con `test_` y deben importarse desde `tests/__ init__.py`, ejemplo.

```
module
|-- ...
|-- tests
    |-- __init__.py
    |-- test_bar.py
    `-- test_foo.py
```

y `__init__.py` contiene:

```python
from . import test_foo, test_bar
```
La prueba simplemente ejecutará cualquier caso de prueba, como se describe en la documentación oficial de la prueba de unittest, pero Odoo proporciona una serie de utilidades y helpers relacionados con la prueba del contenido de Odoo (módulos, principalmente):

`clase odoo.tests.common.TransactionCase (methodName = 'runTest')`

`TestCase` en el que cada método de prueba se ejecuta en su propia transacción y con su propio cursor. La transacción se revierte y el cursor se cierra después de cada prueba.

- `browse_ref (xid)`

	Devuelve un objeto de registro para el identificador externo proporcionado
	- **Parámetros: xid** - identificador externo totalmente calificado, en el formulario `module.identifier`
	- **Aumento:** _ValueError si no se encuentra_
	- **Devoluciones:** `BaseModel`

- `ref (xid)`

	Devuelve el ID de la base de datos para el identificador externo proporcionado, acceso directo para `get_object_reference`
	- **Parámetros: xid** - identificador externo totalmente calificado, en el formulario `module.identifier`
	- **Aumento:** _ValueError si no se encuentra_
	- **Devoluciones:** identificación registrada 
---
`clase odoo.tests.common.SingleTransactionCase (methodName = 'runTest')`

TestCase en el que todos los métodos de prueba se ejecutan en la misma transacción, la transacción se inicia con el primer método de prueba y se revierte al final de la última.

- `browse_ref (xid)`

	Devuelve un objeto de registro para el identificador externo proporcionado
	- **Parámetros: xid** - identificador externo totalmente calificado, en el formulario `module.identifier`
	- **Aumento: ** _ValueError si no se encuentra_
	- **Devoluciones: ** `BaseModel`

- `ref (xid)`

	Devuelve el ID de la base de datos para el identificador externo proporcionado, acceso directo para `get_object_reference`
	- **Parámetros: xid** -identificador externo totalmente calificado, en el formulario `module.identifier`
	- **Aumento:** _ValueError si no se encuentra_
	- **Devoluciones:** identificación registrada 
---
`clase odoo.tests.common.SavepointCase (methodName = 'runTest')`

Similar a `SingleTransactionCase` en que todos los métodos de prueba se ejecutan en una sola transacción, pero cada caso de prueba se ejecuta dentro de un punto de recuperación revertido (subtransacción).

Útil para casos de prueba que contienen pruebas rápidas pero con una configuración de base de datos significativa común a todos los casos (datos de prueba complejos en db): `setUpClass()` se puede usar para generar datos de prueba db una vez, luego todos los casos de prueba usan los mismos datos sin influenciarse entre sí pero sin tener que volver a crear los datos de prueba tampoco.

---
`clase odoo.tests.common.HttpCase (methodName = 'runTest')`

`HTTP TestCase` transaccional con `url_open` y helpers sin cabeza de Chrome.

- `browse_ref (xid)`

	Devuelve un objeto de registro para el identificador externo proporcionado
	- **Parámetros: xid** - identificador externo totalmente calificado, en el formulario `module.identifier`
	- **Aumento:** _ValueError si no se encuentra_ 
	- **Devoluciones:** `BaseModel`
---
`phantom_js (url_path, code, ready = '', login = None, timeout = 60, ** kw)`

- Pruebe el código js que se ejecuta en el navegador - opcionalmente inicie sesión como "inicio de sesión" - cargue la página dada por `url_path` - espere a que esté disponible el objeto listo - eval (código) dentro de la página
- Para señalar la prueba de éxito, haga lo siguiente: `console.log ('ok')`
- Para señalar una falla, haga lo siguiente: `console.log ("error")`

Si ninguno de los dos se realiza antes de que falle la prueba de tiempo de espera.

- `ref (xid)`
	Devuelve el ID de la base de datos para el identificador externo proporcionado, acceso directo para `get_object_reference`
	- **Parámetros xid** - identificador externo totalmente calificado, en el formulario `module.identifier`
	- **Aumento:** _ValueError si no se encuentra_
	- **Devoluciones:** identificación registrada
---

`odoo.tests.common.tagged (*tags)`

Un decorador para etiquetar objetos `BaseCase` Las etiquetas se almacenan en un conjunto al que se puede acceder desde un atributo `'test_tags'`. Una etiqueta con el prefijo ‘-‘ eliminará la etiqueta, p. para eliminar la etiqueta "estándar" De forma predeterminada, todas las clases de prueba de `odoo.tests.common` tienen un atributo `test_tags` que por defecto es "estándar" y también el nombre técnico del módulo Cuando se usa la herencia de clase, las etiquetas NO se heredan.

---

Por defecto, las pruebas se ejecutan una vez justo después de que se haya instalado el módulo correspondiente. Los casos de prueba también se pueden configurar para que se ejecuten después de que se hayan instalado todos los módulos, y no se ejecuten inmediatamente después de la instalación del módulo:
odoo.tests.common.at_install (flag)

Establece el estado de instalación de una prueba, el indicador es un valor booleano que especifica si la prueba debe (Verdadero) o no (Falso) ejecutarse durante la instalación del módulo.

Por defecto, las pruebas se ejecutan justo después de instalar el módulo, antes de comenzar la instalación del siguiente módulo.

En desuso desde la versión 12.0: at_install ahora es un indicador, puede usar tagged () para agregarlo / eliminarlo, aunque tagged solo funciona en clases de prueba
odoo.tests.common.post_install (flag)

Establece el estado posterior a la instalación de una prueba. El indicador es un valor booleano que especifica si la prueba debe o no ejecutarse después de un conjunto de instalaciones de módulos.

Por defecto, las pruebas no se ejecutan después de la instalación de todos los módulos en el conjunto de instalación actual.

En desuso desde la versión 12.0: post_install ahora es un indicador, puede usar tagged () para agregarlo / eliminarlo, aunque tagged solo funciona en clases de prueba




