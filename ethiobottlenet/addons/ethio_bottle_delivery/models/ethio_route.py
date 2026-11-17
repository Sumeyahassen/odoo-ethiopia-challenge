from odoo import models, fields  # type: ignore


class EthioRoute(models.Model):
    _name = 'ethio.route'
    _description = 'EthioBottleNet Delivery Route'
    _order = 'name'

    name = fields.Char(string='Route Name', required=True)
    active = fields.Boolean(default=True)
    stop_ids = fields.One2many(
        'ethio.route.stop',
        'route_id',
        string='Stops'
    )
    note = fields.Text(string='Notes')
