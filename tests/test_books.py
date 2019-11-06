# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.tests import common 




class SampleTest(common.TransactionCase):

    def test_some_action(self):
        books = self.env['library.books']
        author = self.env['library.author']
        category = self.env['library.category']

        books1 = books.create({
            'name': 'Las casas muertas',
            'date_register': '1990-04-18',
            'author_name': '1',
            'category': '1'
        })

        books2 = books.create({
            'name': 'no es tu peo',
            'date_register': '1990-04-19',
            'author_name': '1',
            'category': '1'
        })

        
        
        rsa = author.search([('author_name', '=', 'Jesus')])
        rsc = category.search([('name', '=', 'Fiction')])

        a = self.assertEqual(books1.name, 'Las casas muertas')
        b = self.assertEqual(books2.author_name, rsa)
        self.assertEqual(books1.category, rsc)
        
        print('\n\t\t\t==================================================')
        print('\n\t\t\t========== [ Test realizado con exito ] ==========')
        print('\n\t\t\t==================================================')