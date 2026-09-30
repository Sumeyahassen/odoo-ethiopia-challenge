
from odoo import models, fields # type: ignore #type

class WaterItem(models.Model):
    _name = 'water.item'
    _description = 'Water Product Type'

    name = fields.Char(string='Product Name', required=True)
    capacity = fields.Selection([
        ('0.5l', '0.5 Liter Bottle'),
        ('1l', '1 Liter Bottle'),
        ('2l', '2 Liter Bottle'),
        ('20l', '20L Jerrycan')
    ], string='Volume/Size', required=True)
    unit_price = fields.Float(string='Price per Unit (ETB)', required=True)