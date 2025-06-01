# -*- coding: utf-8 -*-
# from odoo import http


# class AisqnManagement(http.Controller):
#     @http.route('/aisqn_management/aisqn_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aisqn_management/aisqn_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aisqn_management.listing', {
#             'root': '/aisqn_management/aisqn_management',
#             'objects': http.request.env['aisqn_management.aisqn_management'].search([]),
#         })

#     @http.route('/aisqn_management/aisqn_management/objects/<model("aisqn_management.aisqn_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aisqn_management.object', {
#             'object': obj
#         })

