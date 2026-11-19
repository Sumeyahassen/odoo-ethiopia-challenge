from odoo import models, fields  # type: ignore


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    factory_type = fields.Selection([
        ('production', 'Production Factory'),
        ('distribution', 'Distribution Center'),
    ], string='Factory Type', default='distribution')
    contact_id = fields.Many2one(
        'res.partner',
        string='Warehouse Contact'
    )
