from odoo import models, fields, api

class TradingAccount(models.Model):
    _name = 'uni.trading.account'
    _description = 'Trading Account'

    user_id = fields.Many2one('uni.user', string='User', required=True, ondelete='cascade')
    username = fields.Char(string='Username', compute='_compute_username', store=True)
    balance = fields.Float(string='Balance')
    balance_pending = fields.Float(string='Balance Pending')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At')
    update_last_by_id = fields.Many2one('uni.user', string='Updated Last By')
    updated_last_datetime = fields.Datetime(string='Updated Last DateTime')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ], string='Status', default='active')
    investment_plan = fields.Char(string='Investment Plan')
    broker_id = fields.Many2one('uni.broker', string='Broker')
    server = fields.Char(string='Server')

    @api.depends('user_id')
    def _compute_username(self):
        for rec in self:
            rec.username = rec.user_id.username if rec.user_id else False