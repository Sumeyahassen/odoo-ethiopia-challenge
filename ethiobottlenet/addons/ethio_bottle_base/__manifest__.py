{
    'name': 'EthioBottleNet - Base',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Delivery',
    'summary': 'Base module for Ethiopian Bottled Water Distribution System',
    'description': """
        Core configurations, partners, products and multi-factory support
        for EthioBottleNet.
    """,
    'author': 'Your Name / Company',
    'website': 'https://www.yourwebsite.com',
    'depends': [
        'base',
        'product',
        'stock',
        'fleet',
        'contacts',
        'sale_management',
    ],
    'data': [
        'security/ethio_bottle_security.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/res_partner_views.xml',
        'views/product_template_views.xml',
        'views/fleet_vehicle_views.xml',
        'views/stock_warehouse_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}