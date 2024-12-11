from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Grupo(models.Model):
    _name = 'escuela_grupo'  
    _description = 'Grupo de estudiantes' 

    name = fields.Char(string="Nombre del Grupo", required=True)  
    descripcion = fields.Text(string='Descripción')  
    modulo = fields.Selection(
        [('SMR', 'SMR'), ('DAM', 'DAM'), ('DAW', 'DAW'), ('ASIR', 'ASIR')],
        string='Módulo', 
        default='SMR', 
        required=True  
    )
    curso = fields.Selection(
        [('1', '1º Curso'), ('2', '2º Curso')], 
        string='Curso', 
        default='1',
        required=True  
    )
    estudiante_ids = fields.One2many(
        'escuela_estudiante', 
        'grupo_id', 
        string='Estudiantes'
    )  
    
    asignatura_ids = fields.Many2many(
        'escuela_asignatura', 
        string='Asignaturas'
    )  

   

