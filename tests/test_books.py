# -*- coding: utf-8 -*-


from datetime import date
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



        d = (1887,5,7)
        d1 = ('1887','05','07')


        print(books4.date_register.to_date())
        # test assertEqual
        try:
            self.assertEqual(books1.name, 'Mendels Principles of Heredity')
            self.assertEqual(books2.author_name.id, new_author.id)
            self.assertEqual(books3.category.id, new_category.id)
            self.assertEqual(books4.date_register.to_date(), d1)
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


               

        

        