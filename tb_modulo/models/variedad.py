# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Strain(models.Model):
    _name = 'tb_modulo.strain'
    _description = 'Definir una Variedad'

    name = fields.Char(
        'Variedad',
        required=True
    )
    semanas = fields.Selection(
        string='Semanas',
        selection=[('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')],
        default='5'
    )
    descripcion = fields.Text('Descripción')
    precio = fields.Float('Precio')

    bank_id = fields.Many2one('tb_modulo.bank', string='Banco')
