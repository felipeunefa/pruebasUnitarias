# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class LibraryCategory(models.Model): 
    _name = 'library.category' 
    _description = 'Library Category.'

    name = fields.Char(string='Book Category', required=True)
    date_register = fields.Date()
    active = fields.Boolean('Active?', default=True)