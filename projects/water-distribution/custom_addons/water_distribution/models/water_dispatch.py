# -*- coding: utf-8 -*-
from odoo import models, fields, api # type: ignore
from odoo.exceptions import ValidationError # type: ignore

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
    
    # New field to link water items being distributed
    water_item_id = fields.Many2one('water.item', string='Water Product', required=True)
    quantity = fields.Integer(string='Quantity Dispatched', default=1, required=True)

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

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError("The dispatched quantity must be greater than zero!")

    # Workflow Button Actions
    def action_dispatch(self):
        for rec in self:
            rec.state = 'dispatched'

    def action_deliver(self):
        for rec in self:
            rec.state = 'delivered'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'