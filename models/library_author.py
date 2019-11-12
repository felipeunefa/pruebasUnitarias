# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class LibraryAuthor(models.Model): 
    _name = 'library.author' 
    _description = 'Library Author.'

    author_name = fields.Char(required=True)
    date_register = fields.Date()