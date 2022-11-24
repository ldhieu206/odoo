from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_animation(self):
        self.state = 'done'

