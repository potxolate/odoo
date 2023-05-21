# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Blog(models.Model):
    _inherit = 'blog.blog'

    company_id = fields.Many2one('res.company', string='Company', required=True)

class BlogPost(models.Model):
    _inherit = 'blog.post'

    #related field to blog.blog company_id
    company_id = fields.Many2one('res.company', string='Company', related='blog_id.company_id', store=True)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for line in self.order_line:
            if line.product_uom_qty < 1:
                raise ValidationError(('No puede hacer pedidos con cantidad de producto 0.'))
        return super(SaleOrder, self).action_confirm()
    
    def create_wizard(self):
        wizard = self.env['test.model.wizard'].create({
        'test_field': self.name
        })
        return {
            'name': _('Test Wizard'),
            'type': 'ir.actions.act_window',
            'res_model': 'test.model.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }
    
    
class TestModelWizard(models.TransientModel):
    _name =  'test.model.wizard'
    _description = 'Test Model Wizard'
    
    test_field = fields.Char(string = 'Test Field')

    def action_done(self):
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        sale_order.order_line.filtered(lambda line: line.product_uom_qty == 0).unlink()
   
   
class Lead(models.Model):
    _inherit = 'crm.lead'

    fuente = fields.Selection(
        string='Donde nos conoció',
        selection=[('terceros', 'Terceros'), ('rrss', 'Redes sociales'),('serp', 'Búsqueda en Internet')],
        default='serp'
    )