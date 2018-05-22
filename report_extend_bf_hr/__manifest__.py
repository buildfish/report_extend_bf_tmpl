# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Template Report HR',
    'description': 'Template report HR.',
    'summary': 'Export data Odoo to OpenOffice, LibreOffice examples.',
    'category': 'Human Resources',
    'version': '1.0',
    'website': 'http://www.buildfish.com/',
    "license": "AGPL-3",
    'author': 'BuildFish',
    'depends': [
        'report_extend_bf',
        'hr_contract',
    ],
    'data': [
        'data/templates.xml',
        'report.xml',
    ],
    'price': 20.00,
    'currency': 'EUR',
    'images': ['images/main_screenshot.png'],
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
