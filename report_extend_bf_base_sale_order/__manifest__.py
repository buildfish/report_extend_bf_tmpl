# -*- coding: utf-8 -*-

{
    'name': 'Base report sale order',
    'description': 'Base report sale order.',
    'summary': 'Export data Odoo to OpenOffice.',
    'category': 'All',
    'version': '1.0',
    'website': 'http://www.buildfish.com/',
    "license": "AGPL-3",
    'author': 'BuildFish',
    'depends': [
        'report_extend_bf',
        "sale",
        "sale_management",
    ],
    'data': [
        'data/templates.xml',
        'report.xml',
        'views/sale_views.xml'
    ],
    'images': ['images/main_screenshot.png'],
    'application': True,
}
