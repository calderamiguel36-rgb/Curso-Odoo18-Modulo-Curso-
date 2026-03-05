# -*- coding: utf-8 -*-
# from odoo import http


# class Telefono(http.Controller):
#     @http.route('/telefono/telefono', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/telefono/telefono/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('telefono.listing', {
#             'root': '/telefono/telefono',
#             'objects': http.request.env['telefono.telefono'].search([]),
#         })

#     @http.route('/telefono/telefono/objects/<model("telefono.telefono"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('telefono.object', {
#             'object': obj
#         })

