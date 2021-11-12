# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_stock = fields.Float("Minimum stock", default=0)


class ProductProduct(models.Model):
    _inherit = "product.product"

    minimum_stock = fields.Float("Minimum stock", related="product_tmpl_id.minimum_stock")
