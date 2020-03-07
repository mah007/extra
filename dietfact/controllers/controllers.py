# -*- coding: utf-8 -*-
from odoo import http

# class Dietfact(http.Controller):
#     @http.route('/dietfact/dietfact/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dietfact/dietfact/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dietfact.listing', {
#             'root': '/dietfact/dietfact',
#             'objects': http.request.env['dietfact.dietfact'].search([]),
#         })

#     @http.route('/dietfact/dietfact/objects/<model("dietfact.dietfact"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dietfact.object', {
#             'object': obj
#         })