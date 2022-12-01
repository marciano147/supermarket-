# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CartItem(models.Model):
    _name = 'cart.item'
    _description = 'Cart item'

    product_type = fields.Many2one("supermarket.product", string='Product Name')
    quantity = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),
    ('8','8'),('9','9'),('10','10')],string="Quantity")
    add_cart_id = fields.Many2one('customer.cart','owner_cart_id', string="Owner of the Cart")
    total_sum = fields.Integer(string="Total Price of Items", compute='_compute_total', store=True, string='Total Sum of this item')
    price_per_item = fields.Integer(string='Price per Unit', related='product_type.price', store=True, depends=['product_type'])


@api.depends('quantity', 'price')
def _compute_total(self):
    for record in self:
        record.total = record.quantity * record.price

  