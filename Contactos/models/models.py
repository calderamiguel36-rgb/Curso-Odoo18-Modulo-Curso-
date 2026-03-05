# -*- coding: utf-8 -*-
import phonenumbers

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Contactos(models.Model):
    _inherit='res.partner'

    @api.constrains('phone', 'mobile','country_id')
    def verificaion_telefono(self):
        for record in self:
            v = record.phone if record.phone else record.mobile
            if v:
                try:
                    phone_number = phonenumbers.parse(v, record.country_id.code)
                    if not phonenumbers.is_valid_number(phone_number):
                        raise ValidationError(_("El número de teléfono no es válido para el país seleccionado."))
                except phonenumbers.NumberParseException:
                    raise ValidationError(_("El número de teléfono no tiene un formato válido."))

            



#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

