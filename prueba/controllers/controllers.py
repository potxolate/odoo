# -*- coding: utf-8 -*-
# from odoo import http


# class Binovo(http.Controller):
#     @http.route('/binovo/binovo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/binovo/binovo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('binovo.listing', {
#             'root': '/binovo/binovo',
#             'objects': http.request.env['binovo.binovo'].search([]),
#         })

#     @http.route('/binovo/binovo/objects/<model("binovo.binovo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('binovo.object', {
#             'object': obj
#         })
