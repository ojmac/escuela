# -*- coding: utf-8 -*-
# from odoo import http


# class EscuelaMod(http.Controller):
#     @http.route('/escuela_mod/escuela_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuela_mod/escuela_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuela_mod.listing', {
#             'root': '/escuela_mod/escuela_mod',
#             'objects': http.request.env['escuela_mod.escuela_mod'].search([]),
#         })

#     @http.route('/escuela_mod/escuela_mod/objects/<model("escuela_mod.escuela_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuela_mod.object', {
#             'object': obj
#         })

