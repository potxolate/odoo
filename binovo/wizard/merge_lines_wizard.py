# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class MergeLinesWizard(models.TransientModel):
    _name =  'merge.lines.wizard'
    _description = 'Merge Lines Wizard'


    product_id = fields.Many2one('product.product', string='Product')
    
    @api.model
    def _default_order_id(self):
        if self._context.get('active_model') == 'purchase.order' and self._context.get('active_id', False):
            sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
            return sale_order.id    
    
    
    @api.model
    def _default_order_line_ids(self):
        if self._context.get('active_model') == 'purchase.order' and self._context.get('active_id', False):
            sale_order = self.env['purchase.order'].browse(self._context.get('active_id'))
            return sale_order.order_line.ids
    
    order_id = fields.Many2one('purchase.order', string='Order', required=True , default=_default_order_id)
    order_line = fields.Many2many('purchase.order.line', string='Order Lines', required=True, default=_default_order_line_ids)
    
    def merge_lines(self):
        purchase_order_id = self.env['purchase.order'].browse(self._context.get('active_id'))         
        purchase_order_line = self.env['purchase.order.line']
        purchase_order_line.create({
            'order_id': purchase_order_id.id,
            'product_id': self.product_id.id,
            'name': self.product_id.name,
            'product_qty': 1,            
            'price_unit': 1,            
        }) 
        self.order_line.unlink()
        return {'type': 'ir.actions.act_window_close'}