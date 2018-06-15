# -*- coding: utf-8 -*-
{
    'name': 'Reportes Personalizado de Ticket POS',
    # 'description': 'Examples template report.',
    'summary': 'Export data Odoo to OpenOffice, LibreOffice examples.',
    # 'category': 'All',
    'version': '1.0',
    'website': 'http://www.bitodoo.com/',
    "license": "AGPL-3",
    'author': 'Bitodoo',
    'depends': [
        'report_extend_bf',
        "point_of_sale",
    ],
    'data': [
        'data/templates.xml',
        'report.xml',
    ],
    'application': True,
}
