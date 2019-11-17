# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
##############################################################################
from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    # Extend custom report use this method custom_report
    # & return a dictionary values
    def custom_report(self):
        obj_precision = self.env['decimal.precision']
        prec = obj_precision.precision_get('Account')
        lines = []
        for item in self.invoice_line_ids:
            lines.append({
                "product": item.product_id.name,
                "name": item.name,
                "qty": int(item.quantity),
                "image": item.product_id.image_1920,
                "price_unit": format(item.price_unit, ',.%sf' % prec),
                "tax": ', '.join(map(lambda x: (x.name or x.description), item.tax_ids)),
                "price_subtotal": format(item.price_subtotal, ',.%sf' % prec),
                "uom": item.product_uom_id.name,
            })
        values = {
            "invoice_line_ids": lines,
            "untaxed": format(self.amount_untaxed, ',.%sf' % prec),
            "tax": format(self.amount_tax, ',.%sf' % prec),
            "total": format(self.amount_total, ',.%sf' % prec),
            "symbol": self.currency_id.symbol
        }
        return values
