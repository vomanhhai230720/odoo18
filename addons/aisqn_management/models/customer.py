from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _name = 'uni.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')   
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    password = fields.Char(string='Password')
    update_last_by_id = fields.Many2one('res.users', string='Updated Last By')
    updated_last_date_time = fields.Datetime(string='Updated Last Date Time')
    landing_account = fields.Char(string='Landing Account')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    situation = fields.Char(string='Situation')
    tax_residency = fields.Char(string='Tax Residency')
    country = fields.Char(string='Country')
    nationality = fields.Char(string='Nationality') 
    date_of_birth = fields.Date(string='Date of Birth')
    full_address = fields.Char(string='Full Address')
    city = fields.Char(string='City')
    post_code = fields.Char(string='Post Code')
    employment_status = fields.Char(string='Employment Status')
    sources_of_funds = fields.Char(string='Sources of Funds')
    annual_income = fields.Char(string='Annual Income')
    industry = fields.Char(string='Industry')
    purpose_of_investment = fields.Char(string='Purpose of Investment')
    spot_exp = fields.Char(string='Spot Experience')
    feat_exp = fields.Char(string='Feat Experience')
    share_exp = fields.Char(string='Share Experience')
    option_experience = fields.Char(string='Option Experience')
    type_of_document = fields.Char(string='Type of Document')
    document_number = fields.Char(string='Document Number')
    back_identity = fields.Binary(string='Back Identity', attachment=True)
    identity = fields.Binary(string='Identity', attachment=True)
    residence = fields.Binary(string='Residence', attachment=True)
    back_residence = fields.Binary(string='Back Residence', attachment=True)
    user_id = fields.Many2one('uni.user', string='User ID', required=True, ondelete='cascade')

    # Constraints (optional, to ensure uniqueness of username and email)
    _sql_constraints = [
        ('user_id', 'UNIQUE(user_id)', 'The user_id must be unique.'),
    ]

    @api.constrains('user_id')
    def _check_unique_user(self):
        for rec in self:
            existing_profiles = self.search([('user_id', '=', rec.user_id.id), ('id', '!=', rec.id)])
            if existing_profiles:
                raise ValidationError("This user already has a profile.")