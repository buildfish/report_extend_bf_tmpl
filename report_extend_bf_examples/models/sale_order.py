# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def custom_report(self):
        obj_precision = self.env['decimal.precision']
        prec = obj_precision.precision_get('Account')
        lines = []
        for item in self.order_line:
            lines.append(
                {"product": item.name,
                 "qty": int(item.product_uom_qty),
                 "image": item.product_id.image_medium,
                 "price_unit": format(item.price_unit, '.%sf' % prec),
                 "tax": ', '.join(map(lambda x: (x.description or x.name), item.tax_id)),
                 "price_subtotal": format(item.price_subtotal, '.%sf' % prec),
                 })
        values = {
            "order_line": lines,
            "untaxed": format(self.amount_untaxed, '.%sf' % prec),
            "tax": format(self.amount_tax, '.%sf' % prec),
            "total": format(self.amount_total, '.%sf' % prec),
            "symbol": self.pricelist_id.currency_id.symbol
        }
        return values
