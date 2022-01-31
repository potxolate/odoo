# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Bank(models.Model):
    _name = 'tb_modulo.bank'
    _description = 'Banco de variedades'

    name = fields.Char(
        string='Banco',
        required=True
    )

    #    #relacion tablas
    strain_ids = fields.One2many('tb_modulo.strain', 'bank_id', string='Variedades')
