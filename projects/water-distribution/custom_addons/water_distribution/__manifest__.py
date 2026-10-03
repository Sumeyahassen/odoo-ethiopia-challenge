# -*- coding: utf-8 -*-
{
    'name': 'Water Distribution and Fleet Management',
    'version': '17.0.1.0.0',
    'summary': 'Manage water factory distribution, delivery trucks, and sales in Ethiopia',
    'sequence': 10,
    'author': 'Sumeya Hassen',
    'category': 'Operations/Inventory',
    'depends': ['base', 'stock', 'sale_management', 'fleet','hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/water_sequence.xml',
        'views/water_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}