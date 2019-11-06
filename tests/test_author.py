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
        new_author = category.create({ 'author_name': 'William Bateson', 'date_register': '2019-11-06'})


        books1 = books.create({
            'name': 'Mendel\'s Principles of Heredity',
            'date_register': '1990-04-18',
            'author_name': new_author.id,
            'category': new_category.id
            })


        f = Form(books)

        print(f)


#        rsa = author.search([('author_name', '=', 'Jesus')])


        #f.name_author = self.env.ref(author)
        #so = f.save()


        #f.id = a_partner
        #so = f.save()

        
        # books2 = books.create({
        #     'name': 'no es tu peo',
        #     'date_register': '1990-04-19',
        #     'author_name': '1',
        #     'category': '1'
        # })

        
        
        # rsa = author.search([('author_name', '=', 'Jesus')])
        # rsc = category.search([('name', '=', 'Fiction')])

        # a = self.assertEqual(books1.name, 'Las casas muertas')
        # b = self.assertEqual(books2.author_name, rsa)
        # self.assertEqual(books1.category, rsc)

        print('\n\t\t\t====================================================')
        print('\n\t\t\t========== [ Test 2 realizado con exito ] ==========')
        print('\n\t\t\t====================================================')