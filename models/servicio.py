from odoo import models, fields

class Servicio(models.Model):
    _name = 'citas.servicio'
    _description = 'Servicios disponibles para citas'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre del servicio")
    descripcion = fields.Text(string="Descripción", help="Detalles del servicio")
    
    cita_ids = fields.One2many(
        'citas.cita', 
        'servicio_id', 
        string="Citas",
        help="Citas asociadas a este servicio"
    )
    
    usuario_ids = fields.Many2many(
        'citas.usuario',
        string="Usuarios que atienden",
        help="Usuarios que pueden atender este servicio"
    )