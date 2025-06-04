from odoo import models, fields

class Commission(models.Model):
    _name = 'uni.invest.commission'
    _description = 'Commission'

    # wallet_id = fields.Many2one('uni.invest.wallet', string='Wallet', required=True, help='Reference to the wallet (WalletID)')
    wallet_transaction_id = fields.Many2one('uni.invest.wallet_transaction', string='Wallet Transaction', required=True, unique=True)

    base_amount = fields.Float(string='Base Amount', help='Base amount (dựa trên invest của người được mời)')
    base_profit = fields.Float(string='Base Profit', help='Base profit (dựa vào profit người được mời)')
    amount = fields.Float(string='Amount', help='Amount (tính ra thu được nhiều)')   
    inviter_id = fields.Many2one('uni.invest.user', string='Inviter', help='ID-Người mời')
    invitee_id = fields.Many2one('uni.invest.user', string='Invitee', help='ID-Người đích')
