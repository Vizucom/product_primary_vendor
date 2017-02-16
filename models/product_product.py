# -*- coding: utf-8 -*-
from openerp import fields, models, api
import openerp.addons.decimal_precision as dp


class ProductProduct(models.Model):

    _inherit = 'product.product'

    @api.multi
    @api.depends('seller_ids', 'seller_ids.name', 'seller_ids.product_name', 'seller_ids.product_code', 'seller_ids.price', 'seller_ids.currency_id')
    def _compute_primary_vendor(self):

        for product in self:
            if product.seller_ids:
                primary_vendor = product.seller_ids[0]
                product.primary_vendor_id = primary_vendor.name.id
                product.primary_vendor_product_name = primary_vendor.product_name
                product.primary_vendor_product_code = primary_vendor.product_code
                product.primary_vendor_product_price = primary_vendor.price
                product.primary_vendor_product_currency_id = primary_vendor.currency_id.id

    primary_vendor_id = fields.Many2one('res.partner', 'Primary vendor', compute='_compute_primary_vendor')
    primary_vendor_product_name = fields.Char("Primary vendor's product name", compute='_compute_primary_vendor')
    primary_vendor_product_code = fields.Char("Primary vendor's product code", compute='_compute_primary_vendor')
    primary_vendor_product_price = fields.Float("Primary vendor's product price", digits_compute=dp.get_precision('Product Price'), compute='_compute_primary_vendor')
    primary_vendor_product_currency_id = fields.Many2one('res.currency', "Primary vendor's product currency", compute='_compute_primary_vendor')
