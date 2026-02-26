# -*- coding: utf-8 -*-
# from odoo import http


# class CovidCrud(http.Controller):
#     @http.route('/covid__crud/covid__crud', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/covid__crud/covid__crud/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('covid__crud.listing', {
#             'root': '/covid__crud/covid__crud',
#             'objects': http.request.env['covid__crud.covid__crud'].search([]),
#         })

#     @http.route('/covid__crud/covid__crud/objects/<model("covid__crud.covid__crud"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('covid__crud.object', {
#             'object': obj
#         })

