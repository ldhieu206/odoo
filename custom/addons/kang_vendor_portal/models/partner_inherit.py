from odoo import models, fields, api, _


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    vendor_code = fields.Char(string='Vendor Code')
    product_ids = fields.One2many('product.template', 'vendor_code', string='Product')