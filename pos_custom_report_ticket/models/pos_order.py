# -*- coding: utf-8 -*-

from odoo import models
from odoo.exceptions import Warning
from datetime import datetime


class pos_order(models.Model):
    _inherit = "pos.order"

    def custom_report(self):
        date = datetime.strptime(self.date_order, '%Y-%m-%d %H:%M:%S')
        values = {
            "day": date.day,
            "mes": date.month,
            "year": str(date.year)[2:]
            # "amount_to_text": number_to_letter(str(self.amount_total)),
            # "company": self.env.user.company_id.logo,
            # "invoice_line_ids": lines,
            # "untaxed": format(round(self.amount_untaxed, 0), ',.%sf' % prec),
            # "tax": format(round(self.amount_tax, 0), ',.%sf' % prec),
            # "total": format(round(self.amount_total, 0), ',.%sf' % prec),
            # "symbol": self.currency_id.symbol
        }

        # print values
        # raise Warning("ERROR")
        return values