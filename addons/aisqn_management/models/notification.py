from odoo import models, fields

class Notification(models.Model):
    _name = 'uni.invest.notification'
    _description = 'Notification Model'

    customer_id = fields.Many2one('uni.invest.customer', string='Customer', required=True, ondelete='cascade')
    
    type = fields.Selection([
        ('info', 'Info'),
        ('warning', 'Warning'), 
        ('danger', 'Danger')
    ], string='Type', required=True)
    message = fields.Text(string='Message')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    unread = fields.Boolean(string='Unread', default=True)
    title = fields.Char(string='Title')
    action = fields.Selection([
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw')
    ], string='Action')
