from odoo import models, fields, api


class Developer(models.Model):
    _name = 'developer'
    _description = 'Developers Information'

    name = fields.Char(string='Name', required=True)
    position_type = fields.Selection(
        selection=[
            ('front-end', 'Front-End'),
            ('back-end', 'Back-End'),
            ('full-stack', 'Full-Stack'),
            ('out-stuff', 'Out-Stuff')
        ],
        string='Type',
        required=True
    )
    global_identification = fields.Char(string='Global Identification', compute='_compute_global_identification')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    birthdate = fields.Date(string='Birthdate')
    company_id = fields.Many2one(comodel_name='company', string="Company")

    _sql_constraints = [
        ('unique_developer_name', 'unique(name)', 'Developer`s name must be unique.')
    ]

    @api.depends('name', 'position_type')
    def _compute_global_identification(self):
        for rec in self:
            if rec.name and rec.position_type:
                rec.global_identification = f"{rec.name} - {rec.position_type}"
            else:
                rec.global_identification = ""
