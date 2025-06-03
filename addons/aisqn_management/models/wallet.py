from odoo import models, fields, api

class Wallet(models.Model):
    _name = 'uni.wallet'
    _description = 'Wallet'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    currency = fields.Char(string='Currency')
    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='State', default='active')
    account_balance_id = fields.Many2one('uni.account_balance', string='Account Balance')
