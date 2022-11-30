# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductCategory(models.Model):
    _name = 'product.category'
    _description = 'Category'

    type_product = fields.Selection([('1','Fruits'),('2','Vegetables'),('3','Dairy'),('4','Dry'),],string='Type of product',)
   

  