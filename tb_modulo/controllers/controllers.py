# -*- coding: utf-8 -*-
# from odoo import http


# class TbModulo(http.Controller):
#     @http.route('/tb_modulo/tb_modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tb_modulo/tb_modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tb_modulo.listing', {
#             'root': '/tb_modulo/tb_modulo',
#             'objects': http.request.env['tb_modulo.tb_modulo'].search([]),
#         })

#     @http.route('/tb_modulo/tb_modulo/objects/<model("tb_modulo.tb_modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tb_modulo.object', {
#             'object': obj
#         })
