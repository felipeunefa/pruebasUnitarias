# -*- coding: utf-8 -*-


#from datetime import datetime
from odoo.tests.common import TransactionCase

class TestAll(TransactionCase):

    def setUp(self):
        super(TestAll, self).setUp()

        self.books = self.env['library.books']
        self.author = self.env['library.author']
        self.category = self.env['library.category']

        # Create a new category
        self.new_category = self.category.create({ 'name': 'sciences', 'date_register': '1990-04-18'})

        # Create a new author
        self.new_author = self.author.create({ 'author_name': 'William Bateson', 'date_register': '2019-11-06'})

        # Create a news books
        self.books1 = self.books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '1990-04-18',
            'author_name': self.new_author.id,
            'category': self.new_category.id,
            'active': False
            })


        self.books2 = self.books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '1990-04-18',
            'author_name': self.new_author.id,
            'category': self.new_category.id,
            'active': True
            })

        self.books3 = self.books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '2010-06-24',
            'author_name': self.new_author.id,
            'category': self.new_category.id
            })

        self.books4 = self.books.create({
            'name': 'Mendels Principles of Heredity',
            'date_register': '1887-05-07',
            'author_name': self.new_author.id,
            'category': self.new_category.id
            })


    def test_one_create_relationship(self):

        #d = (1887,5,7)

        try:
            self.assertEqual(self.books1.name, 'Mendels Principles of Heredity')
            self.assertEqual(self.books2.author_name.id, self.new_author.id)
            self.assertEqual(self.books3.category.id, self.new_category.id)
            #self.assertEqual(self.books4.date_register, d)
            self.assertEqual(self.books1.active, False)
            
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
