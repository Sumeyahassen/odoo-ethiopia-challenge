{
    'name': "Addis TradeLink - Import Export Extensions",
    'version': '1.0.0',
    'summary': "Custom fields and improvements for Ethiopian Import-Export Trading Companies",
    'description': """
        This module adds useful fields and small improvements
        for Import-Export trading companies in Addis Ababa.
    """,
    'author': "Sumeya Hassen",
    'website': "https://github.com/odoo-ethiopia-challenge/addis_tradelink$",
    'category': 'Inventory/Purchase',
    'depends': [
        'purchase',
        'stock',
        'account',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}