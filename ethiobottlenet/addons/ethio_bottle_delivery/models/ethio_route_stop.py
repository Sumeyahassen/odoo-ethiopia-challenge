from odoo import models, fields # type: ignore


class EthioRouteStop(models.Model):
    _name = 'ethio.route.stop'
    _description = 'Route Stop'
    _order = 'sequence, id'

    route_id = fields.Many2one(
        'ethio.route',
        string='Route',
        required=True,
        ondelete='cascade'
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer / Shop',
        required=True
    )
    delivery_id = fields.Many2one(
        'ethio.delivery.order',
        string='Delivery Order'
    )
    state = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('skipped', 'Skipped'),
    ], string='Status', default='pending')

    note = fields.Char(string='Note')