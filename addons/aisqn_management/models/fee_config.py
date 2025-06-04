from odoo import models, fields

class FeeConfig(models.Model):
    _name = 'uni.invest.fee_config'
    _description = 'Fee Config'

    vps = fields.Float(string='VPS')
    profit_share = fields.Float(string='Profit Share')
    system_fee = fields.Float(string='System Fee')
    asset_fee = fields.Float(string='Asset Fee')
    # currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.company.currency_id.id)
