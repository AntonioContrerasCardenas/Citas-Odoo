# -*- coding: utf-8 -*-

from odoo import models, fields, api


class incidencia(models.Model):
    _name = 'soporte.incidencia'
    _description = 'Modelo para la gestión de incidencias'
    
    
    titulo = fields.Char(
        string='Titulo',
        required = True,
    )
    
    
    description = fields.Html(
        string='Description',
        required = True,
        help='Detalla la incidencia ocurrida brevemente'
    )
    
    
    prioridad = fields.Integer(
        string='Prioridad',
        
        help='Establece un valor mayor o igual a 10 para que se considere una incidencia prioritaria',
        
        default=0
        
    )
    
    
    urgente = fields.Boolean(
        string='urgente',
        readonly=True 
    )
    
    
    cerrada = fields.Boolean(
        string='Cerrada',
    )
    
    '''
    ubicacion = fields.Selection(
        string='Ubicacion',
        selection=[('1', 'Aula1'), ('2', 'Aula2')]
    )
    '''
    
    ubicacion_ids = fields.Many2one(
        string='Ubicacion',
        comodel_name='soporte.ubicacion',
        ondelete='restrict',
    )
    

    archivo = fields.Binary(
        string='Archivo adjunto',
    )
    
    foto = fields.Image(
        
        string='Foto',
        max_width=250
        
    )
    
    
    fecha_creacion = fields.Datetime(
        string='Fecha de creación',
        default=fields.Datetime.now,
    )
    
    
    fecha_modificacion = fields.Date(
        string='Fechade ultima modificación',
        default=fields.Date.context_today,
    )
    
    
    tecnico_ids = fields.Many2many('soporte.tecnico')
    
    

class ubicacion(models.Model):
    _name = 'soporte.ubicacion'
    _descipcion = 'Modelo para almacenar ubicaciones'
    
    
    nombre = fields.Char(
        string='Nombre',
        
        required=True
        
    )
    
    
    pabellon = fields.Selection(
        string='Pabellon',
        selection=[('1', 'Pabellon Paris'), ('1', 'Pabellon Roma')]
    )
    
    
    planta = fields.Selection(
        string='Planta',
        selection=[('1', 'Planta primera'), ('2', 'Planta segunda'), ('3', 'Planta baja')]
    )
    
    
    incidencias_ids = fields.One2many(
        string='Incidencias',
        comodel_name='soporte.incidencia',
    )
    


    

class tecnico(models.Model):
    _name = 'soporte.tecnico'
    _description = 'Modelo para almacenar los datos de los tecnicos'


    nombre = fields.Char(
        string='Nombre',
        required=True,
    )

    
    incidencia_ids = fields.Many2many('soporte.incidencia')
    
    
