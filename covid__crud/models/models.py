# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Covid_CRUD(models.Model):
    _name = 'covid_crud'

    source = fields.Char(string='Source',required=True)
    date = fields.Datetime(string='Date',required=True,default=fields.Datetime.now())
    country_id = fields.Many2one('res.country',required=True,)
    infected = fields.Integer(string='Infecteds',required=True,default=0)
    recovered = fields.Integer(string='Recovered',required=True,default=0)
    deceased = fields.Integer(string='Deceased',required=True,default=0)
    total_infected = fields.Integer(string='Total Infected', compute='set_total_infected',required=True,default=0)
    total_recovered = fields.Integer(string='Total Recovered', compute='set_total_recovered',required=True,default=0)
    total_deceased = fields.Integer(string='Total Deceased', compute='set_total_deceased',required=True,default=0)

    def set_total_infected(self):
        for data in self:
            domain = [
                ('country_id','=',data.country_id.id),
                ('date','<=',data.date),
            ]

            records = self.search(domain)
            infecteds = records.mapped('infected')
            data.total_infected = sum(infecteds) + data.total_infected

    def set_total_recovered(self):
        for data in self:
            domain = [
                ('country_id','=',data.country_id.id),
                ('date','<=',data.date),
            ]

            records = self.search(domain)
            recovereds = records.mapped('recovered')
            data.total_recovered = sum(recovereds) + data.total_recovered
    
    def set_total_deceased(self):
        for data in self:
            domain = [
                ('country_id','=',data.country_id.id),
                ('date','<=',data.date),
            ]

            records = self.search(domain)
            deceaseds = records.mapped('deceased')
            data.total_deceased = sum(deceaseds) + data.total_deceased
    
    def set_percentage_infected(self,):
        total = 0
        if self.total_infected:
            total = (self.infected*100)/self.total_infected
        return total

    def set_percentage_recovered(self,):
        total = 0
        if self.total_infected:
            total = (self.infected*100)/self.total_infected
        return total

    def set_percentage_deceased(self,):
        total = 0
        if self.total_infected:
            total = (self.infected*100)/self.total_infected
        return total


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

