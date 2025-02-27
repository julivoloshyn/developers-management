# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResourceTest(models.Model):
    _description = 'Test Resource Model'
    _name = 'resource.tests'
    _inherit = ['resource.mixin']

    name = fields.Char()
