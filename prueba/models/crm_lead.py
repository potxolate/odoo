# -*- coding: utf-8 -*-

from odoo import models, fields

class Lead(models.Model):
    _inherit = 'crm.lead'

    fuente = fields.Selection(
        string='Donde nos conoció',
        selection=[('terceros', 'Terceros'), ('rrss', 'Redes sociales'),
                   ('serp', 'Búsqueda en Internet')],
        default='serp'
    )