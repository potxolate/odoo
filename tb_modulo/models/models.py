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

from odoo import models, fields, api

class strain(models.Model):
    _name = 'tb_modulo.strain'
    _description = 'Definir una variedad'

    name = fields.Char('Variedad', required=True)
    semanas = fields.Integer(string='Semanas', required=True)
    descripcion = fields.Text('Descripción')

    bank_id = fields.One2many('tb_modulo.bank', string='Banco')

class bank(models.Model):
    _name = 'tb_modulo.bank'
    _description = 'Banco de variedades'

    name = fields.Char(string='Banco', required = True)

    #relacion tablas
    #strain_ids = fields.Many2many('tb_modulo.strain', bank_id, string='Variedades')
