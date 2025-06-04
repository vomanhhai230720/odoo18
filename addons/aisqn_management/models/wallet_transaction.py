from odoo import models, fields, api

class WalletTransaction(models.Model):
    _name = 'uni.invest.wallet_transaction'
    _description = 'Wallet Transaction'

    wallet_id = fields.Many2one('uni.invest.wallet', string='Wallet', required=True)
    fee_managemen_ID = fields.Many2one('uni.invest.fee_management', string='Fee Management')
    name = fields.Char(string='Name')
    type = fields.Selection([
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('profit', 'Profit'),
        ('management', 'Management fee'),
        ('other', 'Other'),
    ], string='Type')
    currency = fields.Char(string='Currency')
    description = fields.Text(string='Description')
    amount = fields.Float(string='Amount', default=0.0) 
    
