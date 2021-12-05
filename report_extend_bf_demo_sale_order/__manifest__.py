# -*- coding: utf-8 -*-

{
    'name': 'Report Templates Demo Sale Order',
    'description': 'Report Templates Demo Sale Order',
    'summary': 'Report Templates Demo Sale Order',
    'category': 'All',
    'version': '1.0',
    'website': 'http://www.build-fish.com/',
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
    ],
    'live_test_url': 'http://report_extend_bf.odoo15.build-fish.com',
    'images': ['static/description/banner.png'],
    'application': True,
}
