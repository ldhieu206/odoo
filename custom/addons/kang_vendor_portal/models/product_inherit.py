from odoo import models, fields, api, _


class ProductInherit(models.Model):
    _inherit = 'product.template'

    vendor_code = fields.Many2one('res.partner', string='Vendor Code')
    deadline = fields.Date(string='Deadline', tracking=True, required=True)
    capacity = fields.Char(string='Capacity', tracking=True, required=True)
    qty_per_box = fields.Integer(string='Qty per box')
    weight = fields.Char(string='Weight')
    height = fields.Float(string='Height')
    length = fields.Float(string='Length')
    width = fields.Float(string='Width')

    # khi nhập weight thì tự động thêm đơn vị là kg
    @api.onchange('weight')
    def _onchange_weight(self):
        if self.weight:
            self.weight = str(self.weight) + ' kg'
