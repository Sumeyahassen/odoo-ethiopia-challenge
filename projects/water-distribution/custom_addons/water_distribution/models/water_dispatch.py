from odoo import models, fields, api # type: ignore

class WaterDispatch(models.Model):
    _name = 'water.dispatch'
    _description = 'Water Distribution Dispatch'
    _rec_name = 'name'

    name = fields.Char(string='Dispatch Reference', required=True, copy=False, readonly=True, default='NEW')
    driver_name = fields.Char(string='Driver Name', required=True)
    truck_plate = fields.Char(string='Truck Plate Number', required=True)
    destination_city = fields.Selection([
        ('addis_ababa', 'Addis Ababa'),
        ('bahir_dar', 'Bahir Dar'),
        ('hawassa', 'Hawassa'),
        ('adama', 'Adama'),
    ], string='Destination City', required=True, default='addis_ababa')
    dispatch_date = fields.Date(string='Dispatch Date', default=fields.Date.today(), required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'NEW') == 'NEW':
            vals['name'] = self.env['ir.sequence'].next_by_code('water.dispatch') or 'NEW'
        return super(WaterDispatch, vals).create(vals)