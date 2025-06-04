from odoo import models, fields

class Broker(models.Model):
    _name = 'uni.invest.broker'
    _description = 'Broker'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
