from odoo import models, fields  # type: ignore


class EthioRouteStop(models.Model):
    _name = 'ethio.route.stop'
    _description = 'EthioBottleNet Route Stop'
    _order = 'sequence, id'

    route_id = fields.Many2one(
        'ethio.route',
        string='Route',
        required=True,
        ondelete='cascade'
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer / Shop',
        required=True
    )
    sequence = fields.Integer(string='Sequence', default=10)
    note = fields.Text(string='Notes')
