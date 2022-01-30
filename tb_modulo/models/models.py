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

from email.policy import default
from odoo import models, fields, api, _


class Socio(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # paciente
    paciente = fields.Boolean("Paciente", default=False)


class Strain(models.Model):
    _name = 'tb_modulo.strain'
    _description = 'Definir una Variedad'

    name = fields.Char('Variedad', required=True)
    semanas = fields.Selection(string='Semanas', selection=[('5','5'),('6','6'),('7','7'),('8','8'),('9','9')], default='5')
    descripcion = fields.Text('Descripción')
    precio = fields.Float('Precio')

    bank_id = fields.Many2one('tb_modulo.bank', string='Banco')


class Bank(models.Model):
    _name = 'tb_modulo.bank'
    _description = 'Banco de variedades'

    name = fields.Char(string='Banco', required=True)

#    #relacion tablas
    strain_ids = fields.One2many('tb_modulo.strain', 'bank_id', string='Variedades')


class Dispensa(models.Model):
    _name = 'tb_modulo.dispensa'
    _description = 'Dispensa'

    cantidad = fields.Char(string='Cantidad', required=True)
    fecha = fields.Date('Fecha', readonly=True, default=fields.date.today())

#    #relacion tablas
    socio_id = fields.Many2one('res.partner', string='Socio', required=True)
    strain_id = fields.Many2one(
        'tb_modulo.strain', string='Variedad', required=True)
