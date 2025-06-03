from odoo import models, fields

class Broker(models.Model):
    _name = 'uni.broker'
    _description = 'Broker'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
