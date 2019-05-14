# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
import pytz

from openerp import models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime


class sale_oder(models.Model):
    _inherit = "sale.order"

    def custom_report(self, **kw):
        obj_precision = self.env['decimal.precision']
        prec = obj_precision.precision_get('Account')

        # Custom date format
        lang = self._context.get("lang")
        record_lang = self.env["res.lang"].search([("code", "=", lang)], limit=1)

        strftime_format = "%s %s" % (record_lang.date_format, record_lang.time_format)

        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
        dt = pytz.UTC.localize(datetime.strptime(self.date_order, DEFAULT_SERVER_DATETIME_FORMAT)).astimezone(user_tz)
        date_order_2 = dt.strftime(strftime_format)

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
            "date_order_2": date_order_2
        }
        return values
