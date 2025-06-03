from odoo import models, fields

class TradingStrategy(models.Model):
    _name = 'uni.trading.strategy'
    _description = 'Trading Strategy'

    profit = fields.Float(string='Profit')
    loss = fields.Float(string='Loss')
    description = fields.Text(string='Description')