# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
import logging
import html
import pytz

from odoo import models, api, fields
from odoo.tools import misc
logger = logging.getLogger(__name__)
try:
    from genshi.core import Markup
except ImportError:
    logger.debug('Cannot import py3o.template')


def format_multiline_value(value):
    if value:
        return Markup(html.escape(value).replace('\n', '<text:line-break/>').
                      replace('\t', '<text:s/><text:s/><text:s/><text:s/>'))
    return ""


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def custom_report(self):
        lang = self._context.get("lang")
        record_lang = self.env["res.lang"].search([("code", "=", lang)], limit=1)
        strftime_format = "%s %s" % (record_lang.date_format, record_lang.time_format)
        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')

        def format_datetime(dt):
            if dt:
                return fields.Datetime.from_string(dt).replace(
                    tzinfo=pytz.utc
                ).astimezone(user_tz).strftime(strftime_format)
            else:
                return ''

        obj_precision = self.env['decimal.precision']
        prec = obj_precision.precision_get('Account')
        lines = []
        for i, line in enumerate(self.order_line):
            lines.append({
                "item": i + 1,
                "product": format_multiline_value(line.name),
                "qty": int(line.product_uom_qty),
                "image": line.product_id.image_medium,
                "price_unit": format(line.price_unit, '.%sf' % prec),
                "tax": ', '.join(map(lambda x: (x.description or x.name), line.tax_id)),
                "price_subtotal": format(line.price_subtotal, '.%sf' % prec),
            })
        values = {
            "order_line": lines,
            "untaxed": format(self.amount_untaxed, '.%sf' % prec),
            "tax": format(self.amount_tax, '.%sf' % prec),
            "total": format(self.amount_total, '.%sf' % prec),
            "symbol": self.pricelist_id.currency_id.symbol,
            "date_order": format_datetime(self.date_order),
            "validity_date": misc.format_date(self.env, self.validity_date, lang_code=self.env.user.lang),
        }
        return values

    @api.multi
    def action_print_offer(self):
        self.ensure_one()
        return self.env.ref('report_extend_bf_examples.action_report_offer_sale_order').report_action(self)
