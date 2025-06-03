from odoo import models, fields

class HistoryDepositBank(models.Model):
    _name = 'uni.history.deposit.bank'
    _description = 'History Deposit Bank'

    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='restrict')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, ondelete='restrict')
    payment_id = fields.Many2one('account.payment', string='Payment', ondelete='set null')
    amount = fields.Float(string='Amount', required=True)
    fee = fields.Float(string='Fee')
    amount_with_fee = fields.Float(string='Amount With Fee', compute='_compute_amount_with_fee')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='pending')
    type = fields.Char(string='Type')
    requested_at = fields.Datetime(string='Requested At')
    confirmed_at = fields.Datetime(string='Confirmed At')
    description = fields.Text(string='Description')
    is_verified_by_admin = fields.Boolean(string='Is Verified By Admin', default=False)

    def _compute_amount_with_fee(self):
        for record in self:
            record.amount_with_fee = (record.amount or 0.0) + (record.fee or 0.0)