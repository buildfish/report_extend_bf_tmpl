# -*- coding: utf-8 -*-

import pytz

from odoo import models, fields


class pos_order(models.Model):
    _inherit = "pos.order"

    def custom_report(self, **kw):
        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
        date = fields.Datetime.from_string(self.date_order).replace(tzinfo=pytz.utc).astimezone(user_tz)

        values = {
            "day": date.day,
            "month": date.month,
            "year": str(date.year)[2:]
        }
        return values
