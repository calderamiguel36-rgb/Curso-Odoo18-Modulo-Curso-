# -*- coding: utf-8 -*-

from odoo import models, fields, api

#ESTE ES MI PRIMER MODELO EN ODOO

class Building(models.Model):
    _name = 'curso.building'
    _description = 'curso.curso'

    name = fields.Char(string='Name',required=True)
    total_floor = fields.Integer(string='Total Floor')
    company_id = fields.Many2one('res.company',string = 'Company',required=True)
    address = fields.Text(string='Address')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

