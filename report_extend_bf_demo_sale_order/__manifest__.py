# -*- coding: utf-8 -*-

{
    'name': 'Report Templates Demo Sale Order',
    'description': 'Report Templates Demo Sale Order',
    'summary': 'Report Templates Demo Sale Order',
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
    'live_test_url': 'http://demo.odoo13.newgalax.com',
    'images': ['static/description/banner.png'],
    'application': True,
}
