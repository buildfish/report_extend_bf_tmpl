# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import fields, models, api


class hr_contract(models.Model):
    _inherit = "hr.contract"

    def custom_report(self):
        values = {
            "company": self.env.user.company_id
        }
        return values
