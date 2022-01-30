# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tb_modulo(models.Model):
#     _name = 'tb_modulo.tb_modulo'
#     _description = 'tb_modulo.tb_modulo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import _, api, fields, models


class Socio(models.Model):
    _inherit = 'res.partner'
    
    paciente = fields.Boolean(default=False , string='Paciente')
   


class Strain(models.Model):
    _name = 'tb_modulo.strain'
    _description = 'Definir una Variedad'

    name = fields.Char('Variedad', required=True)
    semanas = fields.Integer(string='Semanas', required=True)
    descripcion = fields.Text('Descripción')

    banco = fields.Many2many('tb_modulo.bank', string='Banco')


class Bank(models.Model):
    _name = 'tb_modulo.bank'
    _description = 'Banco de variedades'

    name = fields.Char(string='Banco', required=True)

#    #relacion tablas
    strains = fields.Many2one('tb_modulo.strain', string='Variedades',required=True, ondelete='cascade' )
