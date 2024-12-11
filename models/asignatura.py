from odoo import models, fields

class Asignatura(models.Model):
    _name = 'escuela_asignatura'
    _description = 'Asignatura de la escuela'

    codigo = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    horas = fields.Integer(string='Número de horas')
    grupo_ids = fields.Many2many('escuela_grupo', string='Grupos')
