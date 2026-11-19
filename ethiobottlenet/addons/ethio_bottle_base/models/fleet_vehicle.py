
from odoo import models, fields # type: ignore


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    capacity_bottles = fields.Integer(
        string='Capacity (Bottles)',
        help='How many bottles this vehicle can carry'
    )
    capacity_crates = fields.Integer(
        string='Capacity (Crates)',
        help='How many crates this vehicle can carry'
    )
    is_water_truck = fields.Boolean(
        string='Water Distribution Vehicle',
        default=True
    )