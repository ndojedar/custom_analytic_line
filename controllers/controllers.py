# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAnalyticLine(http.Controller):
#     @http.route('/custom_analytic_line/custom_analytic_line/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_analytic_line/custom_analytic_line/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_analytic_line.listing', {
#             'root': '/custom_analytic_line/custom_analytic_line',
#             'objects': http.request.env['custom_analytic_line.custom_analytic_line'].search([]),
#         })

#     @http.route('/custom_analytic_line/custom_analytic_line/objects/<model("custom_analytic_line.custom_analytic_line"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_analytic_line.object', {
#             'object': obj
#         })
