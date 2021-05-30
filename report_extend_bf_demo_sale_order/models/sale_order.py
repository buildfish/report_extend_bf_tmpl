# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
##############################################################################
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    vat_label = fields.Char(related='company_id.vat_label')
    vat_label_full = fields.Char(string='Vat label full', compute="_compute_vat_label")
    # Temporal field
    confirmation_date = fields.Datetime(string='Confirmation Date')

    def _compute_vat_label(self):
        for order in self:
            order.vat_label_full = '%s: %s' % (order.vat_label, order.partner_id.vat) if order.partner_id.vat else ''

    def context_lang(self):
        return self.partner_id.lang


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    image_medium = fields.Binary(related='product_id.image_medium')
