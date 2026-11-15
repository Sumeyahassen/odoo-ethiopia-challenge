
from odoo import models, fields, api, _ # type: ignore
from odoo.exceptions import UserError # type: ignore


class EthioDeliveryOrder(models.Model):
    _name = 'ethio.delivery.order'
    _description = 'EthioBottleNet Delivery Order'
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Reference',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New')
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer / Shop',
        required=True,
        tracking=True
    )
    factory_id = fields.Many2one(
        'res.company',
        string='Factory',
        required=True,
        default=lambda self: self.env.company,
        tracking=True
    )
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        tracking=True
    )
    driver_id = fields.Many2one(
        'res.partner',
        string='Driver',
        domain="[('is_company', '=', False)]",
        tracking=True
    )
    planned_date = fields.Datetime(
        string='Planned Date',
        default=fields.Datetime.now,
        tracking=True
    )
    date_done = fields.Datetime(
        string='Delivery Date',
        readonly=True
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('assigned', 'Assigned'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True, copy=False)

    line_ids = fields.One2many(
        'ethio.delivery.order.line',
        'delivery_id',
        string='Delivery Lines'
    )
    note = fields.Text(string='Notes')
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        related='factory_id',
        store=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('ethio.delivery.order') or _('New')
        return super().create(vals_list)

    def action_assign(self):
        for rec in self:
            if not rec.vehicle_id or not rec.driver_id:
                raise UserError(_('Please select Vehicle and Driver before assigning.'))
            rec.state = 'assigned'

    def action_start_transit(self):
        for rec in self:
            rec.state = 'in_transit'

    def action_deliver(self):
        for rec in self:
            rec.write({
                'state': 'delivered',
                'date_done': fields.Datetime.now()
            })

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'