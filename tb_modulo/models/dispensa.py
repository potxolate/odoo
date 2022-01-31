# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Dispensa(models.Model):
    _name = 'tb_modulo.dispensa'
    _description = 'Dispensa'

    cantidad = fields.Char(
        string='Cantidad',
        required=True
    )
    fecha = fields.Date(
        string='Fecha',
        readonly=True,
        default=fields.date.today()
    )
    #    #relacion tablas
    socio_id = fields.Many2one('res.partner', string='Socio', required=True)
    strain_id = fields.Many2one(
        'tb_modulo.strain', string='Variedad', required=True)
