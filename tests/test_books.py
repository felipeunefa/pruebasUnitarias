# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.tests import common 




class SampleTest(common.TransactionCase):
    def test_some_action(self):
        self.employee = self.env['library.books']

        # create an employee record
        self.employee1 = self.employee.create({
            'name': 'Las casas muertas',
            'date_register': '1990-04-18',
            'author_name': '2',
            'category': '1'
        })

        self.employee2 = self.employee.create({
            'name': 'no es tu peo',
            'date_register': '1990-04-19',
            'author_name': '1',
            'category': '1'
        })

        #self.assertEqual(self.employee1.author_name, '2,')
        #self.assertEqual(self.employee2.date_register, '1990-04-19')

    # def test_compute_employee_designation(self):

    #     self.assertEqual(self.employee1.author_name, 2)

    #     # check position of the employee2
    #     self.assertEqual(self.employee2.date_register, '1990-04-19')

    #     # change the experience of employee2
    #     self.employee2.write({
    #     'name': 'Las casas muertas',
    #     })

    #     # again check the position of employee
    #     self.assertEqual(self.employee2.category, '1')