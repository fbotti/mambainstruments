# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    minimum_stock = fields.Float("Minimum stock", related="product_id.minimum_stock")
