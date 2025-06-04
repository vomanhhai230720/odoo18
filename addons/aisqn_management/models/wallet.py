from odoo import models, fields, api

class Wallet(models.Model):
    _name = 'uni.invest.wallet'
    _description = 'Wallet'

    customer_id = fields.Many2one('uni.invest.customer', string='Customer')    
    name = fields.Char(string='Name')
    type = fields.Selection([
        ('INVEST', 'Invest'),
        ('PROFIT', 'Profit'),
        ('MANAGEMENT', 'Management'),
    ], string='Type')
    currency = fields.Char(string='Currency')
    balance = fields.Float(string='Balance')
    status = fields.Boolean(string='Status')    
    
    
     
    
