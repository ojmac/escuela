# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class escuela_mod(models.Model):
#     _name = 'escuela_mod.escuela_mod'
#     _description = 'escuela_mod.escuela_mod'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

