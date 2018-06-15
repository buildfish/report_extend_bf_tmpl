# -*- coding: utf-8 -*-

from odoo import models
from datetime import datetime


class pos_order(models.Model):
    _inherit = "pos.order"

    def custom_report(self, **kw):
        date = datetime.strptime(self.date_order, '%Y-%m-%d %H:%M:%S')
        values = {
            "day": date.day,
            "month": date.month,
            "year": str(date.year)[2:]
        }
        return values
