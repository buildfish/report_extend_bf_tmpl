# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
##############################################################################

from odoo import fields, models


class Contract(models.Model):
    _inherit = "hr.contract"

    company_id = fields.Many2one(
        'res.company', default=lambda self: self.env.user.company_id)
