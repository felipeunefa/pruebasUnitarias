# -*- coding: utf-8 -*-
{
    'name': 'Libreta de Contactos',
    'category': 'Testing',
    'version': '0.0.1',
    'author': 'hFebles',
    'depends': ['base','web'],
    'data': [
    	#'security/ir.rule.csv',
    	'security/ir.model.access.csv',
    	'views/library_book_view.xml',
    	'views/library_author_view.xml',
    	'views/library_menu.xml',
    	#'views/author_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'demo': [ 'demo/demo.xml',],
}
