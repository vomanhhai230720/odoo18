from odoo import models, fields, api

class AccountBalance(models.Model):
    _name = 'uni.invest.account_balance'
    _description = 'Account Balance'

    user_id = fields.Many2one('uni.user', string='User', required=True)
    amount = fields.Float(string='Amount', default=0.0)
    pending_amount_withdrawal_invest = fields.Float(string='Pending Amount Withdrawal Invest', default=0.0)
    pending_amount_withdrawal_profit = fields.Float(string='Pending Amount Withdrawal Profit', default=0.0)
    pending_amount = fields.Float(string='Pending Amount', default=0.0)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ], string='Status', default='active')
    # currency_id = fields.Many2one('res.currency', string='Currency')
    # created_date_time = fields.Datetime(string='Created Date Time', default=fields.Datetime.now)
    # created_user_id = fields.Many2one('uni.user', string='Created By')
    available_balance = fields.Float(string='Available Balance', compute='_compute_available_balance', store=True)

    @api.depends('amount', 'pending_amount_withdrawal_invest', 'pending_amount_withdrawal_profit', 'pending_amount')
    def _compute_available_balance(self):
        for record in self:
            record.available_balance = record.amount - record.pending_amount_withdrawal_invest - record.pending_amount_withdrawal_profit - record.pending_amount 