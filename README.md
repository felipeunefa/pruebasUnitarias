# Pruebas unitarias Odoo 12


## 1 Instalacion

### Pasos para la instalación:

* Descargar del repositorio oficial el odoo CE  

`$ git clone https://github.com/odoo/odoo.git`

* Cambia el nombre de la carpeta 

`$ mv odoo/ odoo-dev/`

* Ingresa en la carpeta

`$ cd odoo-dev/odoo-dev/`

* Cambia a la version 12.0

`$ git checkout 12.0`

* Instala los requerimientos

`$ sudo pip3 install requeriments.txt`

* Crear el usuario de base de datos

`$ createuser -U postgres usuario -dSRwe`

* Crear la base de datos

`$createdb -U "usuario" "nombre_bd"`

* al finalizar la instalacion de los requerimientos ejecuta el odoo

`$ ./odoo-bin -c test.conf -s --stop-after-init`

## 2 Estructura del directorio
Ahora bien pasaremos a la estructura del directorio existen 2 formas sencillas, la primera es creando el directoriode forma manual y la segunda con el comando `scaffold`

**Comando Scaffold**

`$ ./odoo-bin scaffold "test" "/home/user/odoo-dev/odoo-dev/addons/"`

Generando el siguiente directorio
```
addons/test/
├──controllers
├──demo
├──__init__.py
├──__manifest__.py
├──models
├──security
└──views
```

**Directorios y ficheros importantes**
```
├──__manifest__.py
├──__init__.py
├──models
├──security
└──views
```

Creamos el directorio `tests` para hacer las pruebas

```
$ mkdir tests
```

Quedando de la siguiente forma

```
addons/test/
├──__init__.py
├──__manifest__.py
├──models
├──security
├──tests
└──views
```

## 3 Modulo

### El `__manifest__.py`


```python 
# -*- coding: utf-8 -*-
{
    'name': 'Libreta de Contactos',
    'category': 'Testing',
    'version': '0.0.1',
    'author': 'hFebles',
    'depends': ['base'],
    'data': [
    	'security/ir.model.access.csv',
    	'views/library_book_view.xml',
    	'views/library_author_view.xml',
    	'views/library_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'demo': [ 'demo/demo.xml',],
}
```


### El `__init__.py`

```python
# -*- coding: utf-8 -*-
from . import models
```

### Models/

```
test/models/
├──__init__.py
├──__manifest__.py
├──models
   ├──__init__.py
   ├──library_author.py
   ├──library_books.py
   └──library_category.py
├──security
├──test
└──views

```


#### `test/models/__init__.py`

```python
# -*- coding: utf-8 -*-

from . import library_books, library_author, library_category

```


#### `test/models/library_author`

```python
# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class LibraryAuthor(models.Model): 
    _name = 'library.author' 
    _description = 'Library Author.'

    author_name = fields.Char(required=True)
    date_register = fields.Date()

```

#### `test/models/library_books`

```python
# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class LibraryBooks(models.Model): 
    _name = 'library.books' 
    _description = 'Library Books.'

    name = fields.Char(required=True) 
    author_name = fields.Many2one('library.author', 'Author Name')
    date_register = fields.Date()
    active = fields.Boolean('Active?', default=True)
	category = fields.Many2one('library.category', 'Category Name')

```

#### `test/models/library_category`

```python
# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class LibraryCategory(models.Model): 
    _name = 'library.category' 
    _description = 'Library Category.'

    name = fields.Char(string='Book Category', required=True)
    date_register = fields.Date()
	active = fields.Boolean('Active?', default=True)

```


### Tests/

```
test/models/
├──__init__.py
├──__manifest__.py
├──models
├──security
├──test
   ├──__init__.py
   ├──test_author.py
   └──test_books.py
└──views

```

#### `test/test/__init__.py`
```python 
# -*- coding: utf-8 -*-

from . import test_author
from . import test_books

```

#### `test/test/test_author.py`
```python 
# -*- coding: utf-8 -*-

from odoo.tests import common, Form, tagged

class TestAuthor(common.TransactionCase):

    def test_some_action2(self):
        books = self.env['library.books']
        author = self.env['library.author']
        category = self.env['library.category']

        #create a new category
        new_category = category.create({ 'name': 'sciences', 'date_register': '1990-04-18'})

        #create a new author
        new_author = author.create({ 'author_name': 'William Bateson', 'date_register': '2019-11-06'})


        books1 = books.create({
            'name': 'Mendel\'s Principles of Heredity',
            'date_register': '1990-04-18',
            'author_name': new_author.id,
            'category': new_category.id
            })

        f = Form(books)
        f.name = 'Geometria'
        so = f.save()

        f1 = Form(author)
        f1.author_name = 'Pitagoras'
        so1 = f1.save()

        with Form(so1) as f2:
            f2.author_name = f1.id


        print('\n\t\t\t====================================================')
        print('\n\t\t\t========== [ Test 2 realizado con exito ] ==========')
        print('\n\t\t\t====================================================')

```

#### `test/test/test_author.py`
```python 
# -*- coding: utf-8 -*-


from datetime import datetime
from odoo.tests import common

class AllTest(common.TransactionCase):

    def test_some_action(self):

        books = self.env['library.books']
        author = self.env['library.author']
        category = self.env['library.category']

        # Create a new category
        new_category = category.create({ 'name': 'sciences', 'date_register': '1990-04-18'})

        # Create a new author
        new_author = author.create({ 'author_name': 'William Bateson', 'date_register': '2019-11-06'})

        # Create a news books
        books1 = books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '1990-04-18',
            'author_name': new_author.id,
            'category': new_category.id,
            'active': False
            })


        books2 = books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '1990-04-18',
            'author_name': new_author.id,
            'category': new_category.id
            })

        books3 = books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '2010-06-24',
            'author_name': new_author.id,
            'category': new_category.id
            })

        books4 = books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '1887-05-07',
            'author_name': new_author.id,
            'category': new_category.id
            })


        try:
            self.assertEqual(books1.name, 'Mendels Principles of Heredity')
            self.assertEqual(books2.author_name.id, new_author.id)
            self.assertEqual(books3.category.id, new_category.id)
            self.assertEqual(books1.active, False)
            
        except AssertionError:
            print('\n\t\t\t===========================================================')
            print('\n\t\t\t========== [ Test 1 no fue realizado con exito ] ==========')
            print('\n\t\t\t===========================================================')
            print('\n\t\t\t\t\t========== [ ERRORES ] ==========\n')
            raise
        else:
            print('\n\t\t\t====================================================')
            print('\n\t\t\t========== [ Test 1 realizado con exito ] ==========')
            print('\n\t\t\t====================================================\n')

```

### Views/

```
test/models/
├──__init__.py
├──__manifest__.py
├──models
├──security
├──test
└──views
   ├──author_menu.xml
   ├──library_author_view.xml
   ├──library_book_view.xml
   └──library_menu.xml

```


#### `test/views/author_menu.xml`
```xml
<?xml version="1.0"?> 
<odoo>
  <act_window id="action_library_author" name="Author Books" res_model="library.author" view_mode="tree,form" /> 
  <menuitem id="menu_library_author" name="Books" action="action_library_author" />
</odoo>

```


#### `test/views/library_author_view.xml`

```xml
<?xml version="1.0"?> 
<odoo> 
  <record id="view_form_library_author" model="ir.ui.view"> 
    <field name="name">Authors Information Form</field> 
    <field name="model">library.author</field> 
    <field name="arch" type="xml"> 
      <form string="To-do Task"> 
        <sheet> 
          <group name="group_top"> 
            <group name="group_left">
              <field name="author_name"/>
              <field name="date_register"/>
            </group> 
          </group>
        </sheet>
      </form>
    </field> 
  </record> 
  <record id="view_tree_library_author" model="ir.ui.view"> 
    <field name="name">Author Tree</field> 
    <field name="model">library.author</field> 
    <field name="arch" type="xml"> 
      <tree colors="decoration-muted:is_done==True"> 
        <field name="author_name"/> 
        <field name="date_register"/> 
      </tree> 
    </field> 
  </record>
</odoo>
```


#### `test/views/library_book_view.xml`
```xml
<?xml version="1.0"?> 
<odoo> 
  <record id="view_form_library_book" model="ir.ui.view"> 
    <field name="name">Books Information Form</field> 
    <field name="model">library.books</field> 
    <field name="arch" type="xml"> 
      <form string="To-do Task"> 
        <sheet> 
          <group name="group_top"> 
            <group name="group_left">
              <field name="name"/>
              <field name="date_register"/>
              <field name="category"/>
            </group> 
            <group name="group_right">
              <field name="author_name"/> 
              <field name="active" readonly="1"/> 
            </group> 
          </group>
        </sheet>
      </form>
    </field> 
  </record> 
  <record id="view_tree_library_book" model="ir.ui.view"> 
    <field name="name">Library Tree</field> 
    <field name="model">library.books</field> 
    <field name="arch" type="xml"> 
      <tree colors="decoration-muted:is_done==True"> 
        <field name="name"/> 
        <field name="author_name"/> 
        <field name="category"/> 
        <field name="date_register"/> 
        <field name="active"/> 
      </tree> 
    </field> 
  </record>
</odoo>
```

#### `test/views/library_menu.xml`

```xml
<?xml version="1.0"?> 
<odoo>
  <act_window id="action_library_book" name="Library Books" res_model="library.books" view_mode="tree,form" /> 
  <menuitem id="menu_library_book" name="Books" action="action_library_book" />
  <act_window id="action_library_author" name="Author Books" res_model="library.author" view_mode="tree,form" /> 
  <menuitem id="menu_library_author" name="Author" action="action_library_author" />
</odoo>

```

## 4 Ejecución


`./odoo-bin -c test.conf -i test -d db_test --test-enable`
