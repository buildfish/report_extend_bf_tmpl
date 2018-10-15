# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from odoo import models


class HrContract(models.Model):
    _inherit = "hr.contract"

    def custom_report(self):
        values = {
            "company": self.env.user.company_id
        }
        return values
