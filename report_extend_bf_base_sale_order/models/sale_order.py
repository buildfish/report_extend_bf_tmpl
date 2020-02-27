# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
import logging
import html

from odoo import models, api
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
            "date_order": misc.format_date(self.env, self.date_order, lang_code=self.env.user.lang),
            "validity_date": misc.format_date(self.env, self.validity_date, lang_code=self.env.user.lang),
        }
        return values

    @api.multi
    def action_print_offer(self):
        self.ensure_one()
        return self.env.ref('report_extend_bf_examples.action_report_offer_sale_order').report_action(self)
