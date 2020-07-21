# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
import pytz

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
                 "image": item.product_id.image_128,
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

    def action_print_sale(self):
        self.ensure_one()
        # Return tuple
        # file = self.env.ref('report_extend_bf_examples.action_report_my_sale_order').sudo().render_any_docs([self.id])
        #
        # With data
        # file = self.env.ref('report_extend_bf_examples.action_report_my_sale_order').sudo().render_any_docs([], data={'greeting': "Hello world"})
        #
        # With data
        # return self.env.ref('report_extend_bf_examples.action_report_my_sale_order').report_action([], data={'greeting': "Hello world"})
        return self.env.ref('report_extend_bf_examples.action_report_my_sale_order').report_action(self)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    image_medium = fields.Binary(related='product_id.image_128')