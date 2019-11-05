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