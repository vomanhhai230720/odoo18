from odoo import models, fields

class User(models.Model):
    _name = 'uni.user'  # Model name in Odoo (use a unique name with dot notation)
    _description = 'User Model'  # Description of the model

    # Primary Key (ID is automatically handled by Odoo as 'id', no need to define explicitly)

    # Fields based on the diagram
    username = fields.Char(string='Username', help='Unique username for the user')
    email = fields.Char(string='Email', required=True, help='User email address')
    password = fields.Char(string='Password', required=True, help='User password (hashed)')
    full_name = fields.Char(string='Full Name', help='Full name of the user')
    invite_aff_code = fields.Char(string='Invite Affiliate Code', help='Code for affiliate invitation')
    updated_at = fields.Datetime(string='Update At', help='Last update timestamp')
    phone = fields.Char(string='Phone', help='User phone number')
    updated_last_datetime = fields.Datetime(string='Updated Last DateTime', help='Last updated datetime')
    token = fields.Char(string='Token', help='token')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now, help='Creation timestamp')
    
    # Foreign Key fields (assuming related models exist)
    aff_code = fields.Char(string='Affiliate Code', help='Related affiliate code')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ], string='Status', default='active', help='User account status')
    update_last_by_id = fields.Many2one('uni.user', string='Updated Last By', help='User who last updated this record')

    # Constraints (optional, to ensure uniqueness of username and email)
    _sql_constraints = [
        ('email_unique', 'UNIQUE(email)', 'The email must be unique.'),
    ]