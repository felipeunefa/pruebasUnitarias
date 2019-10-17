# Pruebas unitarias

Como organizar, escribir y ejecutar algunas pruebas de ejemplo en Odoo.

**Intentaré cubrir completamente:**
- Configurar un módulo para pruebas
- Escribir una prueba dentro de los límites del marco de Odoo
- Ejecutando su conjunto de pruebas Odoo / module

## Requisitos
**¿Que necesitas?**
- Una instancia en ejecución de Odoo.
- Un módulo Odoo personalizado (proporcionaré una muestra).
- Haré referencia a Odoo 12, pero Odoo 9 a 12 tienen marcos de prueba bastante similares. No hubo grandes cambios entre las versiones recientes.

## Estructura del módulo

Vamos a crear un módulo de muestra
```
	├── doc
	├── helpers
	├── models
	├── security
	├── static
	├── tests
	├── __manifest__.py
	├── __init__.py
	├── init.xml
	└── readme.md
```

Estoy creando un módulo de muestra llamado test_module que contendrá todas mis pruebas de muestra y código. Verá bastantes directorios arriba, muchos simplemente "estándares" introducidos por Odoo en general, pero el directorio más importante serán las pruebas.

**El directorio de pruebas**
```
test_module/tests/

├── unit
│   ├── test_tweeter_helper.py
│   ├── test_twitter_tweet_model.py
│   ├── test_string_helper.py
│   ├── test_twitter_settings_model.py
│   └── __init__.py
└── __init__.py
```

Puedes organizar tu directorio de pruebas como quieras, pero a menudo intentaré dividir diferentes tipos de pruebas. En el ejemplo anterior, puede ver que tenemos test/unit para todas nuestras pruebas unitarias. Tal vez si continuamos construyendo esto, introduciríamos tests/integration , tests/security, etc.

**Algunos modelos de muestra y helpers**

También dentro de nuestro módulo, tenemos 2 modelos y 2 helpers para usar como ejemplos para escribir algunas pruebas.
Nuevamente, esto es solo una convención para tener una carpeta de modelos y una carpeta de helpers para los módulos de Odoo, pero siempre y cuando sus archivos ``__init__`` estén importando correctamente los archivos, puede organizar su módulo como desee.
```
test_module/helpers
├── string.py
├── tweeter.py
└── __init__.py

test_module/models/
├── twitter
│   ├── tweet.py
│   ├── settings.py
│   └── __init__.py
└── __init__.py
```

## Archivos de módulo
Analicemos el contenido de algunos de estos archivos de muestra que he escrito para usted. No voy a entrar en la carpeta de pruebas hasta la sección a continuación.
**__manifest__.py**
Debido a que estamos usando 12.0, requerimos un archivo de manifiesto. Si estuviéramos mirando 9.0 y viceversa, podríamos tener un archivo __openerp__.py en la raíz de nuestro módulo, pero el contenido general será el mismo.

```python
# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': 'Sample Testing Module',
    'category': 'Testing',
    'version': '12.0.0',
    'author': 'xD',

    # |-------------------------------------------------------------------------
    # | Dependencies
    # |-------------------------------------------------------------------------
    # |
    # | References of all modules that this module depends on. If this module
    # | is ever installed or upgrade, it will automatically install any
    # | dependencies as well.
    # |

    'depends': ['web'],

    # |-------------------------------------------------------------------------
    # | Data References
    # |-------------------------------------------------------------------------
    # |
    # | References to all XML data that this module relies on. These XML files
    # | are automatically pulled into the system and processed.
    # |

    'data': [

        # Security Records...
        'security/ir.rule.csv',
        'security/ir.model.access.csv',

        # General/Data Records...
        'init.xml',
    ],

    # |-------------------------------------------------------------------------
    # | Demo Data
    # |-------------------------------------------------------------------------
    # |
    # | A reference to demo data
    # |

    'demo': [],

    # |-------------------------------------------------------------------------
    # | Is Installable
    # |-------------------------------------------------------------------------
    # |
    # | Gives the user the option to look at Local Modules and install, upgrade
    # | or uninstall. This seems to be used by most developers as a switch for
    # | modules that are either active / inactive.
    # |

    'installable': True,

    # |-------------------------------------------------------------------------
    # | Auto Install
    # |-------------------------------------------------------------------------
    # |
    # | Lets Odoo know if this module should be automatically installed when
    # | the server is started.
    # |

    'auto_install': False,
}
```

**Un par de modelos de muestra**

Tenemos un conjunto de modelos extremadamente creativo y definitivamente único (nadie ha usado Twitter para su tutorial de desarrollo antes, ¿verdad?) Con el que jugar.

El primero es un modelo de configuración de Twitter. Esta será una clase que almacenará un nombre de usuario y una contraseña. Estas serían credenciales para acceder a las cuentas de Twitter si este módulo se expandiera a un módulo funcional.

```python
# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class TwitterSettings(models.Model):
	_name = 'twitter.settings'

	username = fields.Char(string='Username')
	password = fields.Char(string='Password')
	connected = fields.Boolean(string='Connected', default=False)

	def connect(self):
	    """
	    Attempt to connect to Twitter.
	    """
	    self.ensure_one()
	    self.update({'connected': True, })
```

El segundo es un modelo de Tweet. Este es un modelo de datos que contiene la descripción del tweet y las restricciones para el tweet. Por ejemplo, no puede generar un tweet que tenga más de 140 caracteres.
Esto nos da una restricción clara en la que podemos escribir algunas pruebas para garantizar que el sistema aplique la restricción.

```python
# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Tweet(models.Model):
	_name = 'twitter.tweet'
	_rec_name = 'description'

	description = fields.Text(string='Description', size=140, required=True)

	@api.constrains('description')
	def constrain_description(self):
		"""
		Raises a ValidationError if tweets are longer than 140 characters.
		"""
		if self and len(self.description) > 140:
			raise ValidationError('Tweets cannot be longer than 140 characters.')
```

## Escribir una prueba - Requisitos

Muy bien, tenemos un dulce módulo de Twitter construido ahora.
¿Cómo escribimos una prueba para ello? Primero, hay algunos requisitos específicos del marco de prueba de Odoo que debemos cumplir. Verá cómo se aplican en las pruebas de muestra que he escrito, pero esto es lo que necesita pensar:

- Todas las pruebas deben incluirse en las `test/__init__.py`
- Todas las pruebas deben extender una clase de caso de `test` Odoo
- Todas las pruebas deben colocarse dentro del directorio de pruebas en su módulo
- Todos los archivos de prueba deben comenzar con `test_<what_your_testing>.py`
- Todos los métodos de prueba deben comenzar con `def test_<what_your_testing> (self):`

**Todas las pruebas deben incluirse en `tests/__init__.py`**

Incluso si están anidados más profundamente. Entonces, en el caso de nuestro módulo de muestra, tenemos 4 pruebas:

- tests/unit/test_string_helper.py
- tests/unit/test_tweeter_helper.py
- tests/unit/test_twitter_settings_model.py
- tests/unit/test_twitter_tweet_model.py

Si observa el archivo `tests/__init__.py`, verá lo siguiente:

```python
# -*- coding: utf-8 -*-
from .unit import test_string_helper
from .unit import test_tweeter_helper
from .unit import test_twitter_settings_model
from .unit import test_twitter_tweet_model
```

Asegúrese de incluir siempre su archivo de prueba en este archivo `__init__.py` para que el sistema reconozca la prueba.

**Extender una clase de prueba Odoo**

Hay algunas clases de prueba preexistentes con las que puede trabajar, pero debe ampliar una de ellas.

```python
odoo.tests.common.TransactionCase <--- Most common
odoo.tests.common.SingleTransactionCase
odoo.tests.common.HttpCase
odoo.tests.common.SavepointCase
```

Por lo tanto, sus clases de exámenes se verán así:

```python
# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class MyTest(TransactionCase):
```

**Ponga sus pruebas en la carpeta de pruebas**

Puede ser un poco creativo con la organización de su módulo, excepto cuando se trata de cosas como pruebas, asegúrese de que estén en la carpeta de pruebas.
De lo contrario, el marco de prueba los ignorará.

```
test_module/tests/
├── unit
│   ├── test_tweeter_helper.py
│   ├── test_twitter_tweet_model.py
│   ├── test_string_helper.py
│   ├── test_twitter_settings_model.py
│   └── __init__.py
└── __init__.py
```

**Todos los archivos de prueba deben comenzar con test_**

Mientras realiza sus pruebas (y las coloca en la carpeta de pruebas), asegúrese de que todos sus archivos de prueba tengan el prefijo `test_`.

Hay una razón por la cual, en mi ejemplo, mis archivos de prueba tienen nombres como `test_tweeter_helper.py` o `test_string_helper.py`.

**Todos los métodos de prueba deben comenzar con test_**

Todavía no te he mostrado una clase o método de prueba completo, pero cuando agregas métodos a tu clase de prueba (que está dentro de la carpeta de pruebas y dentro de un archivo antepuesto con `tests_<nombre_de_archivo>.py)` entonces también tienes prefijarlo con `test_`.

I know it's feeling a little overkill, but this is the last `test_` you will need.

```python
# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase
class MyTest(TransactionCase):
    def test_should_evaluate_true(self):  <----
        ...
```

## Escribir una prueba - Ejemplos

Ahora ya conoce los 5 requisitos anteriores para escribir una prueba.

Así es como se ve uno:

```python
# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase
from odoo.addons.test_module.helpers import string


class StringHelperTest(TransactionCase):
	def test_string_should_truncate_when_greater(self):
		self.assertEqual(len(string.limit('A short string...', size=5)), 5)

	def test_string_should_do_nothing_when_same_size(self):
		sample_str = 'This is my sample string.'
		sample_str_len = len(sample_str)
		self.assertEqual(len(string.limit(sample_str, sample_str_len)), sample_str_len)

	def test_string_should_do_nothing_when_less_than(self):
		sample_str = 'Another cool sample string!'
		sample_str_len = len(sample_str)
		self.assertEqual(len(string.limit(sample_str, sample_str_len)), sample_str_len)

```

Esta es nuestra prueba de unidad para el helper de strings. Entonces esto está bajo `tests/unit/test_string_helper.py` y está probando nuestro helper en `helpers/string.py`.

No voy a profundizar demasiado en lo que debería intentar probar o en todos los métodos de aserción disponibles para usted (consulte la lista de métodos de aserción para unittest2 o el archivo `odoo/test/common.py` en el núcleo de Odoo.)

Con suerte, puede obtener una idea general del ejemplo anterior sobre cómo escribir algunos métodos de prueba de muestra.

Escribí 3 métodos en ese ejemplo anterior:

1. ¿Nuestro helper de string trunca correctamente una cadena cuando la cadena es más larga que el límite de tamaño?
2. ¿Nuestro helper de string no hace nada cuando la cadena es exactamente el límite de tamaño?
3. ¿Nuestro helper de string no hace nada cuando la cadena es inferior al límite de tamaño?

Para hacer esto, necesito importar nuestro helper de string desde el módulo a través de una llamada de cadena de importación de `odoo.addons.test_module.helpers`, crear algunas cadenas de muestra para trabajar, llamar a la función `string.limit (...)` con la que yo estoy tratando de probar y luego afirmar que los valores de retorno son iguales a los resultados esperados.

```python
def test_string_should_do_nothing_when_same_size(self):
    sample_str = 'This is my sample string.'
    sample_str_len = len(sample_str)
    
    self.assertEqual(
        # Actual results from function call...
        len(string.limit(sample_str, sample_str_len)),
        # Expected results from the function call...
        sample_str_len
    )
```

