from odoo import models, fields

class Cita(models.Model):
    _name = 'citas.cita'
    _description = 'Citas programadas'

    fecha = fields.Date(string="Fecha", required=True, help="Fecha de la cita")
    
    HORARIOS = [
        ('09:00', '09:00 - 09:30'),
        ('09:30', '09:30 - 10:00'),
        ('10:00', '10:00 - 10:30'),
        ('10:30', '10:30 - 11:00'),
        ('11:00', '11:00 - 11:30'),
        ('11:30', '11:30 - 12:00'),
        ('12:00', '12:00 - 12:30'),
        ('12:30', '12:30 - 13:00'),
    ]
    
    horario = fields.Selection(HORARIOS, string="Horario", required=True, help="Horario de la cita")
    
    nombre = fields.Char(string="Nombre", required=True, help="Nombre del contacto")
    email = fields.Char(string="Email", required=True, help="Correo electrónico de contacto")
    telefono = fields.Char(string="Teléfono", required=True, help="Teléfono de contacto")
    
    servicio_id = fields.Many2one(
        'citas.servicio', 
        string="Servicio", 
        required=True, 
        help="Servicio para el que se solicita la cita"
    )
    
    usuario_id = fields.Many2one(
        'citas.usuario', 
        string="Usuario asignado", 
        help="Usuario que atenderá la cita"
    )
    
