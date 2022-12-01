# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductCategory(models.Model):
    _name = 'product.category'
    _description = 'Category'
    # I used a selection field as an example, I suppose it better to have them predefined so the owner of the 
    # supermarket can have some control over it and its not a mess, I know there are categories missing!!
    type_product = fields.Selection([('1','Fruits'),('2','Vegetables'),('3','Dairy'),('4','Dry'),],string='Type of product',)
   

  