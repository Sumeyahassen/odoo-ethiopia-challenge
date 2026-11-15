from odoo import models, fields # type: ignore


class EthioDeliveryOrderLine(models.Model):
    _name = 'ethio.delivery.order.line'
    _description = 'Delivery Order Line'

    delivery_id = fields.Many2one(
        'ethio.delivery.order',
        string='Delivery Order',
        required=True,
        ondelete='cascade'
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )
    quantity = fields.Float(
        string='Quantity',
        default=1.0,
        required=True
    )
    quantity_delivered = fields.Float(
        string='Delivered Qty',
        default=0.0
    )
    uom_id = fields.Many2one(
        'uom.uom',
        string='Unit',
        related='product_id.uom_id',
        store=True
    )