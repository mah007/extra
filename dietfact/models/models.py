# -*- coding: utf-8 -*-

from odoo import models, fields, api
# rebuild this

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_diet = fields.Boolean('Diet item')
    calories = fields.Integer('Calories')

    @api.onchange('calories')
    def _is_diet(self):
        if self.calories <= 100:
            self.is_diet = True
        else:self.is_diet = False




