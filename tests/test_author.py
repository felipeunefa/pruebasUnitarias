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
