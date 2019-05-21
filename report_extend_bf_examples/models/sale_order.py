# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
import pytz

from odoo import models, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def custom_report(self):
        obj_precision = self.env['decimal.precision']
        prec = obj_precision.precision_get('Account')

        # Custom date format
        lang = self._context.get("lang")
        record_lang = self.env["res.lang"].search([("code", "=", lang)], limit=1)

        strftime_format = "%s %s" % (record_lang.date_format, record_lang.time_format)
        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')

        date_order = "- -"
        validity_date = "- -"
        print(self.date_order)
        print(type(self.date_order))
        if self.date_order:
            date_order_dt = pytz.UTC.localize(self.date_order).astimezone(user_tz)
            date_order = date_order_dt.strftime(strftime_format)
        if self.validity_date:
            validity_date_dt = pytz.UTC.localize(self.validity_date).astimezone(user_tz)
            validity_date = validity_date_dt.strftime(strftime_format)

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
            "symbol": self.pricelist_id.currency_id.symbol,
            "date_order": date_order,
            "validity_date": validity_date
        }
        return values

    @api.multi
    def action_print_sale(self):
        self.ensure_one()
        return self.env.ref('report_extend_bf_examples.action_report_my_sale_order').report_action(self)
