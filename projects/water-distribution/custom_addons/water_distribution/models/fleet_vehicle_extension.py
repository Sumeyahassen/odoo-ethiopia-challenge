
from odoo import models, fields # type: ignore

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    # Ethiopian license plate categories (e.g., Code 2, Code 3, Code 01 Federal, etc.)
    plate_prefix_category = fields.Selection([
        ('code_2', 'Code 2 (Automobile / Small Isuzu)'),
        ('code_3', 'Code 3 (Freight / Heavy Cargo Tanker)'),
        ('code_01', 'Code 01 (Federal / Gov)'),
    ], string='Plate Category', default='code_3', required=True)
    
    water_tank_capacity_liters = fields.Float(string='Water Tank Capacity (Liters)', required=True, default=5000.0)
    has_sanitation_certificate = fields.Boolean(string='Food-Grade Sanitation Permit Valid', default=True)