# -*- coding: utf-8 -*-

from odoo import models, fields


class TestModelWizard(models.TransientModel):
    _name = 'test.model.wizard'
    _description = 'Test Model Wizard'

    test_field = fields.Char(string='Test Field')

    def action_done(self):
        sale_order = self.env['sale.order'].browse(
            self._context.get('active_id'))
        sale_order.order_line.filtered(
            lambda line: line.product_uom_qty == 0).unlink()
