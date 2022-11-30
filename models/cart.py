# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.tools import date_utils


class Cart(models.Model):
    _name = 'customer.cart'
    _description = 'Your Cart'
    
    owner_cart_id = fields.Many2one('supermarket.customer','name', string="Choose owner of cart")
    date_creation = fields.Date(string='Date of Cart creation')
    monthtly_period = fields.Float(compute='_monthly_period', string='Time left for premium', store=True, readonly=True)
    total_sum_cart=fields.Float(string='Cart total bill', compute='_total_sum')
    carts_paid = fields.Integer(string='Carts paid already', readonly=True, store=True, compute='_one_paid')
    checked_out = fields.Boolean(compute='_checked_once', string="Amount of checkouts done")
    premium_elegible = fields.Char(readonly=True, compute='_premium_check', string='Are you premium?')


    # Wanted to make this field invisible but found only XML file
    cart_total_products_prices = fields.Many2one('cart.item','total_sum' , readonly=True)






@api.depends('date_creation')
def _monthtly_period(self):
    for record in self:
     add_month = date_utils.add(record.data_creation ,months=1) 
   
@api.depends('cart_total_products_prices')
def _total_sum(self):
    for record in self:
     record.total = record.total + record.cart_total_products_prices

@api.depends('total_sum_cart')
def _one_paid(self):
    for record in self:
     if(record.total_sum_cart != 0 ):
        return 1
     else: 
        return 0


@api.depends('total_sum_cart','carts_paid')
def _checked_once(self):
    for record in self:
      if(record.total_sum_cart ==0 and record.carts_paid==1):
        return 1
      else:
        return 0
         

@api.depends('total_sum_cart', 'checked_out','monthtly_period')
def _premium_check(self):
    today = fields.Datatime.now()
    for record in self:
      if(record.total_sum_cart !=0 and record.checked_out==1 and record.monthly_period > today ):
        return "Allegible for premium"
   
   
   
   





  