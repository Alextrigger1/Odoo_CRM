# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'proyecto.alumno'
    _description = 'Tabla de Alumnos'

    nif = fields.Char(string='NIF', required=True, index=True)
    nombre = fields.Char(string='Nombre')
    apellido1 = fields.Char(string='Apellido1')
    apellido2 = fields.Char(string='Apellido2')
    telefono = fields.Integer(string='Teléfono')
    curso = fields.Char(string='Curso Actual')
    ciclo = fields.Char(string='Ciclo')
    notas = fields.Text(string='Notas')
    
   

    @api.depends('nombre', 'apellido1', 'apellido2')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.nombre} {record.apellido1} {record.apellido2}"
    
    @api.depends('nombre')
    def name_get(self):
        result = []
        for alumno in self:
            result.append((alumno.id, alumno.nombre))
        return result


class Empresa(models.Model):
    _name = 'proyecto.empresa'
    _description = 'Tabla de Empresas'

    cif = fields.Char(string='CIF', required=True, index=True)
    nombre = fields.Char(string='Nombre')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Integer(string='Teléfono')
    persona_contacto = fields.Char(string='Persona de Contacto')
    representante = fields.Char(string='Representante')
    nif_representante = fields.Char(string='NIF Representante')
    convenio = fields.Boolean(string='Convenio')
    notas = fields.Text(string='Notas')
    
    

    @api.depends('nombre')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.nombre}"
            
    @api.depends('nombre')
    def name_get(self):
        result = []
        for empresa in self:
            result.append((empresa.id, empresa.nombre))
        return result
    
class PuestoPractica(models.Model):
    _name = 'proyecto.puesto_practica'
    _description = 'Tabla de Puesto Practica'
    
    empresa_id = fields.Many2one('proyecto.empresa', string='Empresa')
    alumno_id = fields.Many2one('proyecto.alumno', string='Alumno',order=20)
    

    # Campos relacionados para mostrar los atributos correspondientes
    cif_empresa = fields.Char(string='CIF de la Empresa', related='empresa_id.cif', readonly=True)
    nif_alumno = fields.Char(string='NIF del Alumno', related='alumno_id.nif', readonly=True)
    nombre_empresa = fields.Char(string='Nombre de la Empresa', related='empresa_id.nombre', readonly=True)
    nombre_alumno = fields.Char(string='Nombre del Alumno', related='alumno_id.nombre', readonly=True)

   
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    fecha_fin = fields.Date(string='Fecha de Fin')
    horario_manana = fields.Char(string='Horario Mañana')
    horario_tarde = fields.Char(string='Horario Tarde')
    tutor_empresa = fields.Char(string='Tutor de la Empresa')
    relacion_alumno = fields.Boolean(string='Relación con el Alumno')
    notas = fields.Char(string='Notas')
    
    @api.depends('empresa_id', 'alumno_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.nombre_empresa} {record.nombre_alumno}"
    

class Contacto(models.Model):
    _name = 'proyecto.contacto'
    _description = 'Tabla de contactos con Empresa'    

    empresa_id = fields.Many2one('proyecto.empresa', string='Empresa')

    cif_empresa = fields.Char(string='CIF de la Empresa', related='empresa_id.cif', readonly=True)
    nombre_empresa = fields.Char(string='Nombre de la Empresa', related='empresa_id.nombre', readonly=True)

    fecha_contacto = fields.Char(String='Fecha de Contacto')
    tipo_contacto = fields.Char(String='Tipo de Contacto')
    notas = fields.Char(string='Notas')
    
    @api.depends('empresa_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.nombre_empresa} {'- Contacto'}"
    
