from odoo import models, fields

class Estudiante(models.Model):
    _name = 'escuela_estudiante'
    _description = 'Estudiante de la escuela'

    nombre = fields.Char(string="Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required = True)
    edad = fields.Integer(string="Edad")
    asignatura_ids = fields.Many2many('escuela_asignatura', string="Asignaturas")
    grupo_id = fields.Many2one('escuela_grupo', string="Grupo")
