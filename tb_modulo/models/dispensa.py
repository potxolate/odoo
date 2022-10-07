# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Dispensa(models.Model):
    _name = 'tb_modulo.dispensa'
    _description = 'Dispensa'

    cantidad = fields.Integer(
        string='Cantidad',
        required=True,
    )
    fecha = fields.Date(
        string='Fecha',
        readonly=True,
        default=fields.date.today()
    )
    socio_id = fields.Many2one(
        comodel_name='res.partner',
        string='Socio',
        required=True,
    )
    strain_id = fields.Many2one(
        comodel_name='tb_modulo.strain',
        string='Variedad',
        required=True,
    )

    def _compute_total_retirado(self):
        for r in self:
            r.total_retirado = r.strain_id.precio * r.cantidad
            return r.total_retirado

    def _compute_total_dia(self):
        for r in self:
            dispensas = self.env['tb_modulo.dispensa'].search([
                ('fecha', '=', r.fecha)
            ])
            for disp in dispensas:
                r.total_dia += disp.cantidad * disp.strain_id.precio
            return r.total_dia

    total_retirado = fields.Float(
        string='Total Retirado',
        compute=_compute_total_retirado,
    )
    total_dia = fields.Float(
        string='Total Dia',
        compute=_compute_total_dia,
    )

    def name_get(self):
        resultados = []
        for r in self:
            descripcion = f'{len(r)} dispensa - {r.total_retirado} €'
            resultados.append((r.id, descripcion))
        return resultados
