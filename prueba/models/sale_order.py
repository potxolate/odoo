# -*- coding: utf-8 -*-

from odoo import models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for line in self.order_line:
            if line.product_uom_qty < 1:
                raise ValidationError(
                    ('No puede hacer pedidos con cantidad de producto 0.'))
        return super(SaleOrder, self).action_confirm()

    def create_wizard(self):
        wizard = self.env['test.model.wizard'].create({     
        })
        return {
            'name': ('Borrar Productos con cantidad 0'),
            'type': 'ir.actions.act_window',
            'res_model': 'test.model.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }