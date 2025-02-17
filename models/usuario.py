from odoo import models, fields

class Usuario(models.Model):
    _name = 'citas.usuario'
    _description = 'Usuarios que atienden citas'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre del usuario que atiende citas")
    email = fields.Char(string="Email", required=True, help="Correo electrónico del usuario")
    telefono = fields.Char(string="Teléfono", help="Teléfono de contacto")
    foto = fields.Image(string="Foto", help="Imagen del usuario")

    servicio_ids = fields.Many2many(
        'citas.servicio', 
        string="Servicios que atiende",
        help="Servicios que puede atender el usuario"
    )
