# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class incidencia(models.Model):
    _name = 'soporte.incidencia'
    _description = 'Modelo para la gestión de incidencias'
    
    def informe_incidencia_boton(self):
        return self.env.ref('soporte.action_informe_incidencias').report_action(self)
    
    titulo = fields.Char(
        string='Titulo',
        required = True,
        default='Incidencia X'
    )
    
    
    description = fields.Html(
        string='Description',
        required = True,
        help='Detalla la incidencia ocurrida brevemente'
    )
    
    
    prioridad = fields.Integer(
        string='Prioridad',
        
        help='Establece un valor entre 0 y 10. Si el valor es mayor de 7 será urgente',
        
        default=0
        
    )
    
    
    urgente = fields.Boolean(
        string='urgente',
        compute='_compute_urgente' ,
        store=True
        )
         
    @api.depends('prioridad')
    def _compute_urgente(self):
        for record in self:
            if record.prioridad > 7:
                record.urgente = True
            else:
                record.urgente = False
    
    cerrada = fields.Boolean(
        string='Cerrada',
        
        default=False
        
    )
    
    
    @api.constrains('prioridad')
    def _check_prioridad(self):
        for record in self:
            if record.prioridad > 10:
                raise ValidationError('Error en la prioridad. Debe ser un valor entre 0 y 10')
            
            
            
    
    
    
    
    '''
    ubicacion = fields.Selection(
        string='Ubicacion',
        selection=[('1', 'Aula1'), ('2', 'Aula2')]
    )
    '''
    
    ubicacion_id = fields.Many2one(
        string='Ubicacion',
        comodel_name='soporte.ubicacion',
        ondelete='restrict',
    )
    

    archivo = fields.Binary(
        string='Archivo adjunto',
    )
    
    foto = fields.Image(
        
        string='Foto',
        max_width=250,
        max_height=250
        
    )
    
    
    fecha_creacion = fields.Datetime(
        string='Fecha de creación',
        default=fields.Datetime.now(),
    )
    

    fecha_modificacion = fields.Datetime(
        string='Fechade ultima modificación',
        default=lambda self: fields.Datetime.now(),
    )
    
    @api.onchange('titulo', 'description', 'prioridad' ,'ubicacion_id', 'cerrada', 'archivo')
    def _onchange_fecha_modificacion(self):
        for record in self:
            record.fecha_modificacion = fields.Datetime.now()
    
    
    tecnico_ids = fields.Many2many('soporte.tecnico')
    
    
    _sql_constraints = [
        (
            'intervalo_prioridad',
            'CHECK (prioridad >= 0 AND prioridad < 11)',
            'La prioridad debe ser un valor entre 0 y 10'
        )
    ]
    
    

class ubicacion(models.Model):
    _name = 'soporte.ubicacion'
    _description = 'Modelo para almacenar las ubicaciones'
    
    _rec_name = 'nombre'
    nombre = fields.Char(
        string='Nombre',
        
        required=True
        
    )
    
    
    pabellon = fields.Selection(
        string='Pabellon',
        selection=[('1', 'Pabellon Paris'), ('2', 'Pabellon Roma')]
    )
    
    
    planta = fields.Selection(
        string='Planta',
        selection=[('0', 'Planta primera'), ('1', 'Planta segunda'), ('2', 'Planta baja')]
    )
    
    
    incidencias_ids = fields.One2many(
        string='Incidencias',
        comodel_name='soporte.incidencia',
        inverse_name='ubicacion_id'  # ← Añade esta línea
    )
    


    

class tecnico(models.Model):
    _name = 'soporte.tecnico'
    
    # _inherit = ['soporte.tecnico']
    
    _description = 'Modelo para almacenar las personas que reparan incidencias'

    _rec_name='nombre'
    
    
    # tipo = fields.Selection(
    #     string='Tipo',
    #     selection=[('0', 'Tec.general'), ('1', 'Tec.Hardware'), ('2', 'Tec.Software'), ('3', 'Tec.Servicios')]
    # )
    
    
    nombre = fields.Char(
        string='Nombre',
        required=True,
    )

    
    incidencia_ids = fields.Many2many('soporte.incidencia')
    
    
