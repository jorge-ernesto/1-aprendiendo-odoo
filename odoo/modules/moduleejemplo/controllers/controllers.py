# -*- coding: utf-8 -*-
# from odoo import http


# class Moduleejemplo(http.Controller):
#     @http.route('/moduleejemplo/moduleejemplo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moduleejemplo/moduleejemplo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('moduleejemplo.listing', {
#             'root': '/moduleejemplo/moduleejemplo',
#             'objects': http.request.env['moduleejemplo.moduleejemplo'].search([]),
#         })

#     @http.route('/moduleejemplo/moduleejemplo/objects/<model("moduleejemplo.moduleejemplo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moduleejemplo.object', {
#             'object': obj
#         })

