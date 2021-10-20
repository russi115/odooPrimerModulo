from odoo import models, fields

class author(models.Model):
    _name= 'author'

    name = fields.Char(String="author")