from odoo import models, fields


class Company(models.Model):
    _name = 'company'
    _description = 'Companies Information'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    developer_ids = fields.One2many(string='Developers', inverse_name='company_id', comodel_name='developer')
