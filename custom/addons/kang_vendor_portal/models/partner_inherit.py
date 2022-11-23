from odoo import models, fields, api, _


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    vendor_code = fields.Char(string='Vendor Code')