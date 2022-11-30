# -*- coding: utf-8 -*-
from odoo import fields, models


class Product(models.Model):
    _name = 'supermarket.product'
    _description = 'Description'

    name = fields.Char('Name')
    category_id = fields.Many2one('product.category', 'type_product', string='Category')
    price = fields.Char('Unit price')
    
    

  