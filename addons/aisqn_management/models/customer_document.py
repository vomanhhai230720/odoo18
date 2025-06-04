from odoo import models, fields, api

class CustomerDocument(models.Model):
    _name = 'uni.invest.customer.document'
    _description = 'Customer Document'

    user_id = fields.Many2one('uni.invest.user', string='User', required=True, ondelete='cascade')
    username = fields.Char(string='Username', compute='_compute_username', store=True)
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    file = fields.Binary(string='File', attachment=True)
    file_name = fields.Char(string='File Name')

    @api.depends('user_id')
    def _compute_username(self):
        for rec in self:
            rec.username = rec.user_id.username if rec.user_id else False