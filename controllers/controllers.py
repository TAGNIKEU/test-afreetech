# -*- coding: utf-8 -*-
from odoo import http

# class GestionGic(http.Controller):
#     @http.route('/gestion_gic/gestion_gic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_gic/gestion_gic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_gic.listing', {
#             'root': '/gestion_gic/gestion_gic',
#             'objects': http.request.env['gestion_gic.gestion_gic'].search([]),
#         })

#     @http.route('/gestion_gic/gestion_gic/objects/<model("gestion_gic.gestion_gic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_gic.object', {
#             'object': obj
#         })