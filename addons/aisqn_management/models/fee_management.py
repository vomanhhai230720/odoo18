from odoo import models, fields

class FeeManagement(models.Model):
    _name = 'uni.invest.fee_management'
    _description = 'Fee Management'

    wallet_transaction_id = fields.Many2one('uni.invest.wallet_transaction', string='Wallet Transaction', required=True, unique=True)
    fee_config_id = fields.Many2one('uni.invest.fee_config', string='Fee Config')
    # wallet_id = fields.Many2one('uni.invest.wallet', string='Wallet', required=True)
    amount = fields.Float(string='Amount', help='Calculated amount to be used in wallet transaction')
    invested = fields.Float(string='Invested')
    profit = fields.Float(string='Profit')

    _sql_constraints = [
        ('wallet_transaction_id', 'unique (wallet_transaction_id)', 'The wallet transaction ID must be unique.'),
    ]
