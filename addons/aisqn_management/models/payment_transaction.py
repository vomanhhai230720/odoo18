from odoo import models, fields

class PaymentTransaction(models.Model):
    _name = 'uni.payment.transaction'
    _description = 'Payment Transaction'

    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='restrict')
    payment_id = fields.Many2one('account.payment', string='Payment', ondelete='set null')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, ondelete='restrict')
    amount = fields.Float(string='Amount', required=True)
    fee = fields.Float(string='Fee')
    amount_with_fee = fields.Float(string='Amount With Fee', compute='_compute_amount_with_fee')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='pending')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At')
    created_by_user_id = fields.Many2one('res.users', string='Created By User')
    updated_by_user_id = fields.Many2one('res.users', string='Updated By User')
    type = fields.Selection([
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
    ], string='Type')
    requested_at = fields.Datetime(string='Requested At')
    confirmed_at = fields.Datetime(string='Confirmed At')
    desc = fields.Text(string='Description')
    is_verified_by_admin = fields.Boolean(string='Is Verified By Admin', default=False)

    def _compute_amount_with_fee(self):
        for record in self:
            record.amount_with_fee = (record.amount or 0.0) + (record.fee or 0.0)
            
class PaymentTransactionCrypto(models.Model):
    _name = 'uni.payment.transaction.crypto'
    _description = 'Payment Transaction Crypto'

    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='restrict')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, ondelete='restrict')
    network = fields.Char(string='Network')
    from_address = fields.Char(string='From Address')
    to_address = fields.Char(string='To Address')
    tx = fields.Char(string='Transaction Hash')
    amount = fields.Float(string='Amount', required=True)
    fee = fields.Float(string='Fee')
    amount_with_fee = fields.Float(string='Amount With Fee', compute='_compute_amount_with_fee')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='pending')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At')
    updated_by_user_id = fields.Many2one('res.users', string='Updated By User')
    created_by_user_id = fields.Many2one('res.users', string='Created By User')
    type = fields.Selection([
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
    ], string='Type')
    requested_at = fields.Datetime(string='Requested At')
    confirmed_at = fields.Datetime(string='Confirmed At')
    desc = fields.Text(string='Description')
    is_verified_by_admin = fields.Boolean(string='Is Verified By Admin', default=False)

    def _compute_amount_with_fee(self):
        for record in self:
            record.amount_with_fee = (record.amount or 0.0) + (record.fee or 0.0)

class PaymentMethod(models.Model):
    _name = 'uni.payment.method'
    _description = 'Payment Method'

    affiliate_id = fields.Many2one('res.users', string='Affiliate', ondelete='set null')
    referred_id = fields.Many2one('res.users', string='Referred', ondelete='set null')
    amount = fields.Float(string='Amount')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ], string='Status', default='pending')