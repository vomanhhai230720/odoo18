from odoo import models, fields, api

class WalletTransaction(models.Model):
    _name = 'uni.wallet_transaction'
    _description = 'Wallet Transaction'

    wallet_id = fields.Many2one('uni.wallet', string='Wallet', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    note = fields.Text(string='Note')
    amount = fields.Float(string='Amount', default=0.0)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], string='Status', default='pending')
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now)
